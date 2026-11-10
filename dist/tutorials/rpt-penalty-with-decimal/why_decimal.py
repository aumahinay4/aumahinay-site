"""Why money should not be stored as float."""

from decimal import Decimal

print(0.10 + 0.20)                         # float
print(Decimal("0.10") + Decimal("0.20"))   # Decimal

# Add one centavo a hundred thousand times
total_float = 0.0
total_decimal = Decimal("0.00")
for _ in range(100_000):
    total_float += 0.01
    total_decimal += Decimal("0.01")

print(total_float)
print(total_decimal)
