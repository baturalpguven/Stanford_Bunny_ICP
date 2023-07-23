# <a href="http://graphics.stanford.edu/data/3Dscanrep/"> Stanford Bunny </a> ICP
In this repository, the point2plane ICP algorithm is applied to Stanford Bunny and visualized with matplotlib.



## ICP

First, let’s start with the implementation of PCA, this method is one of the most common feature reduction methods that preserve the variance of the dataset by choosing the most relevant features via assessing their eigenvectors as much as possible. Due to this reason, it was an important tool to use in our work. The mathematical model of PCA can be summarized as 



The objective function to minimize is given by:

$$E = \sum_i \left(\mathbf{n_i} \cdot \left(\mathbf{R_\theta} \mathbf{p_i} + \mathbf{t} - \mathbf{q_j}\right)\right)^2 \rightarrow \mathrm{min},$$

where:
- \(\mathbf{n_i}) is the normal vector of the i-th point in the source point cloud.
- \(\mathbf{R_\theta}) is the 2D rotation matrix with angle \(\theta\).
- \(\mathbf{p_i}) is the i-th point in the source point cloud.
- \(\mathbf{t}) is the translation vector.
- \(\mathbf{q_j}) is the j-th point in the target point cloud.

The derivative of \(E\) with respect to \(\theta\) is given by:

$$\displaystyle \frac{\partial E}{\partial \theta} = \left[\begin{matrix}n_{x} & n_{y} & n_{x} \left(- p_{x} \sin{\theta} - p_{y} \cos{\theta}\right) + n_{y} \left(p_{x} \cos{\theta} - p_{y} \sin{\theta}\right)\end{matrix}\right].$$





## Results


<table>
  <tr>
    <td align="center">
      <img src="https://github.com/baturalpguven/Stanford_Bunny_ICP/assets/77858949/aa91c3cf-4a26-4d56-90f9-526bd6351844" alt="Before" >
    </td>
    <td align="center">
      <img src=https://github.com/baturalpguven/Stanford_Bunny_ICP/assets/77858949/2a69f220-448b-4bff-b03d-23a137a9df61" alt="After" >
    </td>
  </tr>
</table>


## Running the Code
To run the code simply run the following in the command line for training.

```
python3 icp.py ./bunny/bun045.pts ./bunny/bun000.pts
python3 icp.py ./bunny/bun090.pts ./bunny/bun045.pts
python3 icp.py ./bunny/bun315.pts ./bunny/bun000.pts
python3 icp.py ./bunny/bun270.pts ./bunny/bun315.pts
python3 icp.py ./bunny/bun180.pts ./bunny/bun270.pts
python3 icp.py ./bunny/chin.pts ./bunny/bun315.pts
python3 icp.py ./bunny/ear_back.pts ./bunny/bun180.pts
python3 icp.py ./bunny/top2.pts ./bunny/bun180.pts
python3 icp.py ./bunny/top3.pts ./bunny/bun000.pts

```

To generate the bunny image after ICP run following

```
python3 view_pts_3D_matplotlib.py -- mode output
```

To generate the bunny image after ICP run following
```
python3 view_pts_3D_matplotlib.py -- mode bunny
```


Replace ` view_pts_3D_matplotlib.py`, and ` icp.py` with the name of your script or executable. The `--mode` is an example command-line argument that you can customize based on your specific use case.

Command Line Arguments:

--mode <str> (default: 'output')
    For After ICP: output for Before ICP: bunny


Feel free to modify the example command and arguments to match the specific command line interface of your project.



## Referances

1. <a href="https://github.com/ReillyBova/Point-Cloud-Registration/tree/master"> Point-Cloud-Registration </a>
2. <a href="https://www.youtube.com/watch?v=QWDM4cFdKrE"> Iterative Closest Point (ICP) - 5 Minutes with Cyrill </a>
3. <a href="https://nbviewer.org/github/niosus/notebooks/blob/master/icp.ipynb"> Jupyter/nbviewer/ICP </a>








