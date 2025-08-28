Galaxy Column Extractor Tool
This repository contains a custom Galaxy tool, "Extract Columns", which allows a user to extract specific columns from a CSV file by number.

The project is structured to demonstrate the full lifecycle of Galaxy tool development, including:

A standalone Python script for the core logic (csv_extract_python_package/).

A Conda recipe for packaging the script (recipes/).

The Galaxy tool wrapper and test files (csv_extract_tool/).

How to Run This Tool
To use this tool in your own Galaxy instance, you need to perform two main setup steps: install the tool's code and install its software dependency.

Prerequisites
A running local instance of Galaxy.

Conda installed on your system.

Step 1: Install the Tool in Galaxy
You need to move the tool's wrapper files into your Galaxy server's tools directory so it can be found.

Navigate to the directory where you cloned this project.

Copy the csv_extract_tool directory into your Galaxy installation's tools folder. For example:

# Example:
cp -r path/to/GALAXY_COLUMN_EXTRACTOR_TOOL/csv_extract_tool path/to/your/galaxy/tools/

Step 2: Install the Software Dependency
The tool relies on a custom Conda package to run its script. You must install this package from the public Anaconda.org channel where it is hosted.

Open your terminal. It's recommended to activate the Conda environment your Galaxy instance uses, but you can also install it in your base environment.

Run the following command to install the csv_extract package from the nathnael_d channel:

conda install -c nathnael_d csv_extract

Step 3: Run Galaxy and Use the Tool
Start your Galaxy server. If it's already running, you will need to restart it for it to recognize the new tool.

Find the tool. Once Galaxy has started, look in the "Tools" panel on the left. You should find a new tool named "Extract Columns".

Use it! You can now use this tool in your analyses just like any other standard Galaxy tool.

Development & Testing
If you wish to modify or test this tool, you can use Planemo. The necessary test files are included in the csv_extract_tool/test-data/ directory.

To run the automated tests, navigate to the csv_extract_tool directory and run:

planemo test
# Galaxy Column Extractor Tool

This repository contains a custom Galaxy tool, **"Extract Columns"**, which allows a user to extract specific columns from a CSV file by number.

The project is structured to demonstrate the full lifecycle of Galaxy tool development, including:
* A standalone Python script for the core logic (`csv_extract_python_package/`).
* A Conda recipe for packaging the script (`recipes/`).
* The Galaxy tool wrapper and test files (`csv_extract_tool/`).

![Project Structure](https://i.imgur.com/3GAgL9g.png)

---

## How to Run This Tool

To use this tool in your own Galaxy instance, you need to perform two main setup steps: install the tool's code and install its software dependency.

### Prerequisites

* A running local instance of Galaxy.
* Conda installed on your system.

### Step 1: Install the Tool in Galaxy

You need to move the tool's wrapper files into your Galaxy server's `tools` directory so it can be found.

1.  Navigate to the directory where you cloned this project.
2.  Copy the `csv_extract_tool` directory into your Galaxy installation's `tools` folder. For example:

    ```bash
    # Example:
    cp -r path/to/GALAXY_COLUMN_EXTRACTOR_TOOL/csv_extract_tool path/to/your/galaxy/tools/
    ```

### Step 2: Install the Software Dependency

The tool relies on a custom Conda package to run its script. You must install this package from the public Anaconda.org channel where it is hosted.

1.  Open your terminal. It's recommended to activate the Conda environment your Galaxy instance uses, but you can also install it in your base environment.
2.  Run the following command to install the `csv_extract` package from the `nathnael_d` channel:

    ```bash
    conda install -c nathnael_d csv_extract
    ```

---

### Step 3: Run Galaxy and Use the Tool

1.  **Start your Galaxy server.** If it's already running, you will need to restart it for it to recognize the new tool.
2.  **Find the tool.** Once Galaxy has started, look in the "Tools" panel on the left. You should find a new tool named **"Extract Columns"**.
3.  **Use it!** You can now use this tool in your analyses just like any other standard Galaxy tool.

### Development & Testing

If you wish to modify or test this tool, you can use Planemo. The necessary test files are included in the `csv_extract_tool/test-data/` directory.


To run the automated tests, navigate to the `csv_extract_tool` directory and run:

```bash
planemo test
```


To run the galaxy instance on locally

```bash
planemo serve
```