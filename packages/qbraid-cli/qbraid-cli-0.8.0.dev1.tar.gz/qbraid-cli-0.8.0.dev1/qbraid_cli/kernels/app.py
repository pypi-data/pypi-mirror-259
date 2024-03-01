"""
Module defining commands in the 'qbraid jobs' namespace.

"""

import typer

app = typer.Typer(help="Manage qBraid kernels.")


@app.command(name="list")
def kernels_list():
    """List all available kernels."""
    from jupyter_client.kernelspec import KernelSpecManager

    kernel_spec_manager = KernelSpecManager()
    kernelspecs = kernel_spec_manager.get_all_specs()

    if len(kernelspecs) == 0:
        print("No qBraid kernels active.")
        # print("\nUse 'qbraid kernels add' to add a new kernel.")
        return

    longest_kernel_name = max(len(kernel_name) for kernel_name in kernelspecs)
    spacing = longest_kernel_name + 10

    print("# qbraid kernels:")
    print("#")
    print("")

    # Ensure 'python3' kernel is printed first if it exists
    python3_kernel_info = kernelspecs.pop("python3", None)
    if python3_kernel_info:
        print("python3".ljust(spacing) + python3_kernel_info["resource_dir"])

    # Print the rest of the kernels
    for kernel_name, kernel_info in sorted(kernelspecs.items()):
        print(f"{kernel_name.ljust(spacing)}{kernel_info['resource_dir']}")


if __name__ == "__main__":
    app()
