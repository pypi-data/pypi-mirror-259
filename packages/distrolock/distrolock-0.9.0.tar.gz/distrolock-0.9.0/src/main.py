import tkinter as tk
import tkinter.ttk as ttk
import traceback
from PIL import ImageTk, Image
import requests
import json
from threading import *
import time
import os


class SoftwareVoidedException(Exception):
    """
    This exception is raised when the software is void and can no longer be used.
    """
    pass


class DistroLock:
    """
    Serverless distributable authentication.
    """
    def __init__(self, configuration, passwordTransformer):
        """
        Initialize distrolock with necessary configuration
        :param configuration: a map with configuration options. See official documentation for more details.
        :param passwordTransformer: callback to transform user entered password into stored result
        """

        self.productName = configuration["productName"]
        self.version = configuration["version"]
        self.securityPolicyURL = configuration["securityPolicyURL"]
        self.securityPolicy = None
        self.DEBUG_MODE = self.__getProperty(configuration, "debug", default=True)
        self.win_title = self.__getProperty(configuration, "win_title", default="distrolock: authorize")
        self.win_icon = self.__getProperty(configuration, "win_icon", default="../defaults/icon.ico")
        self.win_img_left = self.__getProperty(configuration, "win_img_left", default="../defaults/banner.png")
        self.win_img_top = self.__getProperty(configuration, "win_img_top", default="../defaults/banner-top.png")
        self.passwordTransformer = passwordTransformer

        self.__log('debug mode is enabled. Make sure to turn off in production.')

    def __log(self, msg):
        """
        prints debug messages, if enabled
        :param msg: debug message
        """
        if self.DEBUG_MODE:
            print(f'[distrolock] {msg}')

    @staticmethod
    def __getProperty(obj, prop, default=None):
        """
        Retrieves property from map with defaulting
        :param obj: map
        :param prop: key, value of which to be retrieved
        :param default: returned value if key does not exist
        :return: obj[prop] || default
        """
        if prop in obj:
            return obj[prop]
        else:
            return default

    def authorize(self):
        """
        Prompt the user for authorization. This is a blocking operation.
        Should an error occur, or the user fails to authenticate, the program will not advance further.
        """
        global authFeedbackLabel, authenticated, errorOccurred

        root = self.__createBaseWindow()

        contentFrame = tk.Frame(root)
        contentFrame.configure(background='#e2e2e0')
        contentFrame.grid(sticky="NW", column=1, row=0, pady=(150, 0))

        pb = ttk.Progressbar(contentFrame, length=300, mode='indeterminate')
        pb.grid(sticky="ws", column=1, row=0, pady=(0, 50))
        pb.start(10)

        authFeedbackLabel = None
        errorOccurred = False
        authenticated = False

        def fetchAuthDetails(tkRoot, progressBar):
            global authFeedbackLabel, authenticated, errorOccurred

            try:
                contents = self.__getSecurityPolicy()
                self.securityPolicy = contents
                parsedContent = json.loads(contents)
                expectedResult = parsedContent[self.productName][self.version]
                if expectedResult == "VOID":
                    raise SoftwareVoidedException

                progressBar.destroy()

                label = tk.Label(contentFrame, text="Enter password:", font=('Segoe UI', 11))
                label.configure(background='#e2e2e0')
                label.grid(sticky="nw", column=1, row=0, pady=(0, 0))

                ttk.Style(root).configure('padded.TEntry', padding=[5, 3, 5, 3])
                passwordInput = ttk.Entry(contentFrame, width=47, style='padded.TEntry', show="*")
                passwordInput.grid(sticky="nw", column=1, row=0, pady=(30, 0))

                def authenticateAsync():
                    global authFeedbackLabel, authenticated, validAuth

                    if authFeedbackLabel is not None:
                        authFeedbackLabel.destroy()
                    authButton["state"] = "disabled"
                    time.sleep(0.5)
                    authButton["state"] = "enabled"

                    userPassword = passwordInput.get()
                    userResult = self.passwordTransformer(userPassword)
                    validAuth = False
                    if type(expectedResult) is list:
                        validAuth = userResult in expectedResult
                    else:
                        validAuth = userResult == expectedResult
                    if not validAuth:
                        self.__log(
                            f'denied authentication attempt [{userPassword}] with transformed result [{userResult}]')
                        authFeedbackLabel = tk.Label(contentFrame, text="Incorrect credentials.", font=('Segoe UI', 11),
                                                     fg='red', wraplength=310)
                        authFeedbackLabel.configure(background='#e2e2e0')
                        authFeedbackLabel.grid(sticky="nw", column=1, row=0, pady=(90, 0))
                    else:
                        self.__log(
                            f'accepted authentication attempt [{userPassword}] with transformed result [{userResult}]')
                        authFeedbackLabel = tk.Label(contentFrame, text="Successfully authenticated. Starting up...",
                                                     font=('Segoe UI', 11), fg='green',
                                                     wraplength=310)
                        authFeedbackLabel.configure(background='#e2e2e0')
                        authFeedbackLabel.grid(sticky="nw", column=1, row=0, pady=(90, 0))
                        authButton["state"] = "disabled"
                        authenticated = True
                        time.sleep(2)
                        tkRoot.after(0, tkRoot.destroy)

                def authenticate():
                    authThread = Thread(target=authenticateAsync)
                    authThread.start()

                authButton = ttk.Button(contentFrame, text="Authenticate", command=authenticate)
                authButton.grid(sticky="ne", column=1, row=0, pady=(60, 0), ipadx=10)
            except Exception as e:
                for widget in contentFrame.winfo_children():
                    widget.destroy()
                errorMessage = None
                errorType = type(e)
                if errorType == requests.exceptions.ConnectionError:
                    errorMessage = "Network error. Please fix your connection and try again."
                elif errorType == json.decoder.JSONDecodeError or errorType == KeyError:
                    errorMessage = "The server sent malformed data. This is not your fault."
                elif errorType == SoftwareVoidedException:
                    errorMessage = "This software has been terminated and may no longer be used."
                errorLabelText = f"A fatal error has occurred\n[ID: {e.__class__.__name__}]" if errorMessage is None else errorMessage
                errorLabel = tk.Label(contentFrame, text=errorLabelText, font=('Segoe UI', 11), fg='red',
                                      wraplength=310)
                errorLabel.configure(background='#e2e2e0')
                errorLabel.grid(sticky="nw", column=1, row=0, pady=(0, 0))
                errorOccurred = True

                if self.DEBUG_MODE:
                   traceback.print_exc()

        mainThread = Thread(target=fetchAuthDetails, args=([root, pb]), daemon=True)
        mainThread.start()
        root.mainloop()

        if errorOccurred or not authenticated:
            quit()

    def startPeriodicScan(self, interval=60):
        """
        Periodically scan for changes in the security policy for real-time termination.
        If a change is detected, the program is terminated forcefully.
        :param interval: interval for which scans are performed
        """
        def periodicScan():
            while True:
                time.sleep(interval)
                policy = self.__getSecurityPolicy()
                if policy != self.securityPolicy:
                    self.__log('detected change in security policy')
                    root = self.__createBaseWindow()

                    contentFrame = tk.Frame(root)
                    contentFrame.configure(background='#e2e2e0')
                    contentFrame.grid(sticky="NW", column=1, row=0, pady=(150, 0))

                    errorLabelText = ("distrolock has detected a change in security policy and needs to restart. "
                                      "This window will automatically close in 10 seconds.")
                    errorLabel = tk.Label(contentFrame, text=errorLabelText, font=('Segoe UI', 11), fg='red',
                                          wraplength=310)
                    errorLabel.configure(background='#e2e2e0')
                    errorLabel.grid(sticky="nw", column=1, row=0, pady=(0, 0))

                    root.after(10000, root.destroy)
                    root.mainloop()
                    os._exit(1)
                else:
                    self.__log('no changes detected in security policy')

        scanThread = Thread(target=periodicScan, daemon=True)
        scanThread.start()

    def __createBaseWindow(self):
        """
        Creates the base window (with images)
        """
        # prevent garbage collection
        global logo, banner

        root = tk.Tk()
        root.configure(background='#e2e2e0')
        root.iconbitmap(self.win_icon)
        root.wm_attributes('-topmost', True)
        root.resizable(False, False)
        root.title(self.win_title)

        logo = ImageTk.PhotoImage(Image.open(self.win_img_left))
        logoPanel = tk.Label(root, image=logo)
        logoPanel.configure(background='#e2e2e0')
        logoPanel.grid(column=0, row=0, padx=(0, 20))

        banner = ImageTk.PhotoImage(Image.open(self.win_img_top))
        bannerPanel = tk.Label(root, image=banner)
        bannerPanel.configure(background='#e2e2e0')
        bannerPanel.grid(sticky="N", column=1, row=0, pady=(40, 0), padx=(0, 20))
        return root

    def __getSecurityPolicy(self):
        """
        Retrieves the security policy
        :return: the HTTP GET response from the security policy URL
        """
        self.__log(f'retrieving security policy from {self.securityPolicyURL}')
        response = requests.get(self.securityPolicyURL)
        contents = response.content.decode()
        self.__log(f'retrieved content: [{contents}] from {self.securityPolicyURL}')
        return contents