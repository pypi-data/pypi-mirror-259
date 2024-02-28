commands: list[str] = []
packages: list[str] = []


def need(command: str) -> None:
    match command:
        case 'debootstrap':
            package = 'debootstrap'
        case 'mksquashfs' | 'unsquashfs':
            package = 'squashfs-tools'
        case _:
            package = None
    if package:
        if package not in packages:
            packages.append(package)
