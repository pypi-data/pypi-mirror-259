import cmd
import ps

cmd.need('grub-mkimage')

COMPRESSION = 'xz'
ENV_BYTES = 1024
ENV_COMMENT = '#'
ENV_HEADER = f'''{ENV_COMMENT} GRUB Environment Block
'''
MODULES = {
    'i386-pc': [
        ('biosdisk',),
        ('ntldr',),
    ]
}


def make_image(image_format: str, image_path: str, modules: list[str],
               memdisk_path: str, pubkey_path: str = None) -> None:
    args = [
        ('grub-mkimage',),
        ('--compress', COMPRESSION),
        ('--format', image_format),
        ('--output', image_path),
        ('--memdisk', memdisk_path),
    ]
    if pubkey_path:
        args.append(('--pubkey', pubkey_path))
    args.extend(modules)
    if modules := MODULES.get(image_format, None):
        args.extend(modules)
    ps.run(*args)
