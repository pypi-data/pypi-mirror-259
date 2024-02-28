import ps
import rwx.cmd

rwx.cmd.need('mksquashfs')


def mksquashfs(input_root: str, output_file: str):
    ps.run([
        'mksquashfs',
        input_root,
        output_file,
        '-comp', 'zstd',
        '-Xcompression-level', str(18),
    ])
