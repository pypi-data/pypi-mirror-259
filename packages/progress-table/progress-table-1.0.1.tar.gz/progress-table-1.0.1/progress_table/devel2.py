import random
import sys
import time

from progress_table import ProgressTableV1

# Create table object:
table = ProgressTableV1()

# Or customize its settings:
table = ProgressTableV1(
    columns=["step"],
    refresh_rate=10,
    num_decimal_places=4,
    default_column_width=None,
    default_column_color=None,
    default_column_alignment=None,
    default_column_aggregate=None,
    default_row_color=None,
    embedded_progress_bar=True,
    pbar_show_throughput=True,
    pbar_show_progress=False,
    print_row_on_update=True,
    reprint_header_every_n_rows=30,
    custom_format=None,
    table_style="round",
    file=sys.stdout,
)

# You can define the columns at the beginning
table.add_column("x", width=3)
table.add_column("x root", color="red")
table.add_column("random average", color=["bright", "red"], aggregate="mean")

for step in table(iter(range(100))):
    x = random.randint(0, 200)

    # There are two ways to add new values:
    table["x"] = x
    table["step"] = step
    # Second:
    table.update("x root", x**0.5)
    table.update("x squared", x**2)

    # Display the progress bar by wrapping the iterator
    for _ in range(10):  # -> Equivalent to `table(range(10))`
        # You can use weights for aggregated values
        table.update("random average", random.random(), weight=1)
        time.sleep(0.02)

    # Go to the next row when you're ready
    table.next_row()

# Close the table when it's ready
table.close()

# Export your data
data = table.to_list()
pandas_df = table.to_df()  # Requires pandas to be installed
np_array = table.to_numpy()  # Requires numpy to be installed
