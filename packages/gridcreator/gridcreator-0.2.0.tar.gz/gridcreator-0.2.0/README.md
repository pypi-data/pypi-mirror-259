# What does that library can do?

This library is designed for creating grids to facilitate the decentralization of different products. It is currently being developed as a gridnet library with integrated network functions.

# How to install?

```
pip install gridcreator
```

# How to use?

```
import grid
my_grid = grid.Grid()
network = grid.Network("test", my_grid)

account = grid.Account()
account_1 = grid.Account()
network.import_account(account)
network.import_account(account_1)
print(my_grid.get)
```

### To be updated...
