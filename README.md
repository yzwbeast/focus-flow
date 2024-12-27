# Study Progress Tracker

[中文版本 README available here](README.zh.md)

## This project is an integrated version of the following three projects
- **[entodo](https://github.com/yzwbeast/entodo)**：[based on a weekly plan with tasks for reading, writing, listening, speaking, and vocabulary. Log progress, view achievements, and visualize completion.](https://github.com/yzwbeast/entodo/blob/main/README.md)
- **[pomodoro](https://github.com/yzwbeast/pomodoro)**：[It lets you set timers, add tags, and view daily statistics and charts. Supports English and Chinese, with data backup.](https://github.com/yzwbeast/pomodoro/blob/main/README.md)
- **[read-log](https://github.com/yzwbeast/read-log)**：[A simple and efficient book tracking program to log and manage your reading records.](https://github.com/yzwbeast/read-log/blob/main/README.md)

## Installation
1. Clone the repository and enter the project directory:
   ```bash
   git clone https://github.com/yzwbeast/focus-flow.git
   cd focus-flow
   ```
2. Create a virtual environment

   <details>
   <summary>Why Use Virtual Environments</summary>

   > When you encounter the "**externally-managed-environment**" error, it might be because the Python version installed via APT by the operating system enforces strict management of the system environment, preventing users from modifying system-level Python packages with pip.<br />
   > **Recommended Solution**:<br />Using a virtual environment is the cleanest and safest method. It does not affect the system Python environment and allows you to freely manage dependencies.
   </details>

   Run in the project directory:
   ```bash
   python3 -m venv flow
   ```
   - `flow` is the name of the virtual environment and can be replaced with any name.
3. Activate the virtual environment:
   ```bash
   source flow/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the script:
   ```bash
   python x.py
   ```
6. Exit the virtual environment: After use, you can exit the environment:
   ```bash
   deactivate
   ```
7. Delete the virtual environment
Just delete the my_env folder:
   ```bash
   rm -rf flow
   ```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

[中文版本 README available here](README.zh.md)
