# Public Address Generator
Generate EVM public address from mnemonic-phrase or private key.

# Installation 
```
pip install public_address_generator
```

# Usage 

```
a_g = public_address_generator.MnemonicConverter(mnemonic)
pub_address = a_g.get_evm_address(1)
```

# TODO
Currently EVM only addresses are suported. BTC and LTC addresses will be added in the next update.
