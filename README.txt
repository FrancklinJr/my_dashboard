# Interactive Dashboard Project

This project is an interactive dashboard built using [Dash](https://dash.plotly.com/), a Python framework for building web applications. The dashboard allows users to upload CSV files, visualize the data through interactive graphs, and explore the data with various filtering options.

## Features

- **File Upload**: Users can upload CSV files to visualize the data.
- **Interactive Graphs**: Visualize data with interactive bar charts.
- **Dynamic Dropdowns**: Choose columns for the X-axis, Y-axis, and optional grouping.
- **Modular Structure**: Organized codebase for maintainability and scalability.

## Project Structure

my_dashboard/
│
├── app.py
├── assets/
│ └── (CSS and JS files)
├── data/
│ └── (CSV data files)
├── callbacks/
│ ├── init.py
│ ├── update_output.py
│ └── update_graph.py
├── components/
│ ├── init.py
│ └── layout.py
├── utils/
│ ├── init.py
│ └── parse_contents.py
└── requirements.txt

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/my_dashboard.git
    cd my_dashboard
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application**:
    ```bash
    python app.py
    ```

2. **Open the application**:
    Open your web browser and go to `http://127.0.0.1:8050/`.

3. **Upload a CSV file**:
    - Drag and drop a CSV file or click to select a file.
    - Use the dropdowns to select columns for the X-axis, Y-axis, and optional grouping.
    - View the interactive graph.

## Examples

Here are a few examples of how to use the dashboard:

### Example 1: Simple Bar Chart

1. Upload a CSV file with columns such as `Category`, `Value`.
2. Select `Category` for the X-axis and `Value` for the Y-axis.
3. View the bar chart displaying values for each category.

### Example 2: Grouped Bar Chart

1. Upload a CSV file with columns such as `Category`, `Subcategory`, `Value`.
2. Select `Category` for the X-axis, `Value` for the Y-axis, and `Subcategory` for grouping.
3. View the bar chart with grouped bars.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Dash](https://dash.plotly.com/)
- [Plotly](https://plotly.com/)