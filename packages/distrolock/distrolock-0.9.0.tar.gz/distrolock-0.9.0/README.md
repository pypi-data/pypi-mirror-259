<p align="center">
    <img src="resources/logo-github.png" />
</p>
<h3 align="center">Serverless distributable authentication</h3>
<p align="center">Add authentication security to your distributables without a server.</p>

**Features:**

- 🔒 authenticate users for distributables with _any_ static site generator (e.g., Github Pages) - no custom server needed!
- ❌ revoke/terminate distributables remotely and in <ins>real time</ins>

**When is this needed?**

If you are sharing distributables and don't want unauthorized users to use it, or if you want the ability to revoke access to your distributable. 

## How it works

![](resources/diagram.png)

**distrolock** authenticates by sending a GET request (not POST) to **retrieve** the security policy.

Once the security policy has been retrieved, **the authentication happens client side.** On paper this is insecure,
but once compiled into an `exe` and obfuscated with tools like `pyarmor` it requires strong technical knowledge to bypass<sup>1</sup>.

The security policy looks like this:

```json
{
  "product-1": {
    "version-1": "VOID",
    "version-2": "3b0e98ef7923166602d7a9f327782eea090454960cf8bfe1af3b9c8620cd5680"
  },
  "product-2": {
    "version-1": ["ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb", "3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d"]
  }
}
```

> [!TIP]
> We recommend you host your security policy on online SSG's like Github Pages, where it will automatically rebuild when the policy is changed.

## Gallery

| Main Screen                   | Network Error                    | Terminated Script             |
|-------------------------------|----------------------------------|-------------------------------|
| ![](resources/demos/main.png) | ![](resources/demos/network.png) | ![](resources/demos/void.png) |

_Note_: the images can be customized!

## Tutorial

Prepend a few lines of code and you're good to go!

```python
def transformer(password):
    return sha256(password.encode()).hexdigest()


lock = DistroLock({
    "productName": "product",
    "version": "v1.0.0",
    "securityPolicyURL": "https://colonelparrot.github.io/distrolock/policy-example.json",
}, transformer)
lock.authorize() # present challenge (correct answer [asdf123])
lock.startPeriodicScan() # check for security policy changes for real-time termination

# ... your code
```

For more in-depth documentation, please visit the [wiki](https://github.com/ColonelParrot/distrolock/wiki).

### Remarks
<sup>1</sup> this tool is designed to be a solution that works out-of-the-box. It can stop _most_ people,
even some tech-savvy individuals.