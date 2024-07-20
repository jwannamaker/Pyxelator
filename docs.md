# mpl_toolkits

----

## mpl_toolkits.mplot3d.proj3d.inv_transform(*xs, ys, zs, invM*)

Transform the points by the inverse of the projection matrix, `invM`.

## mpl_toolkits.mplot3d.proj3d.proj_transform(*xs, ys, zs, M*)

Transform the points by the transformation matrix, `M`.

- `xs`: array of x values
- `ys`: array of y values
- `zs`: array of z values
- `M`: 3x3 array maybe 4x4 array?

## mpl_toolkits.mplot3d.proj3d.proj_transform_clip(*xs, ys, zs, M*)

Transform the points by the projection matrix, `M` and return the clipping result.

## mpl_toolkits.mplot3d.proj3d.world_transformation(*xmin, xmax, ymin, ymax, zmin, zmax, pb_aspect=None*)

Produce a matrix that scales homogenous points in the specified ranges to [0, 1] or [0, pb_aspect[i]] if the plotbox aspect ratio is specified.

```python
def world_transformation(xmin, xmax, ymin, ymax, zmin, zmax, pb_aspect=None):
    dx = xmax - xmin
    dy = ymax - ymin
    dz = zmax - zmin
    if pb_aspect is not None:
        ax, ay, az = pb_aspect
        dx /= ax
        dy /= ay
        dz /= az

    return np.array([[1/dx, 0,    0,    -xmin/dx],
                     [0,    1/dy, 0,    -ymin/dy],
                     [0,    0,    1/dz, -zmin/dz],
                     [0,    0,    0,    1]])
```
