[Xiaoli Wang<sup>1</sup>](https://github.com/lily983){:target="_blank"}, [Sipu Ruan<sup>1</sup>](https://ruansp.github.io/){:target="_blank"}, [Xin Meng<sup>1</sup>](https://github.com/XinnMeng){:target="_blank"}, 
[Hongtao Wu<sup>1</sup>](https://github.com/ChirikjianLab){:target="_blank"},
[Wanze Li<sup>1</sup>](https://github.com/ChirikjianLab){:target="_blank"},
[Zhanhong Sun<sup>1</sup>](https://github.com/ChirikjianLab){:target="_blank"},
[Yuwei Wu<sup>1</sup>](https://github.com/ChirikjianLab){:target="_blank"},
[Ceng Zhang<sup>1</sup>](https://github.com/ChirikjianLab){:target="_blank"},
[Wan Su<sup>1</sup>](https://github.com/ChirikjianLab){:target="_blank"}, 
[Chen Dong<sup>2</sup>](https://github.com/ChirikjianLab){:target="_blank"}, 
[Cecilia Laschi<sup>12*</sup>](https://scholar.google.com/citations?user=1vR7lMUAAAAJ&hl=en){:target="_blank"}
[Gregory Chirikjian<sup>12*</sup>](https://cde.nus.edu.sg/me/staff/chirikjian-gregory-s/){:target="_blank"}

<sup>1</sup>Department of Mechanical Engineering, National University of Singapore, Singapore

<sup>2</sup>Department of Mechanical Engineering, University of Delaware, USA

<sup>*</sup>Principal Investigator


## Motivation: Learning Affordances Through Play
Just like this monkey experimenting with stones, humans learn to use tools by playing, testing, and discovering their affordances. A stick can become a lever, a rock can become a hammer — but this is not taught directly. Instead, it emerges through interaction and imagination.

This project takes inspiration from this natural process. Our goal is to enable robots to:

- Imagine possible uses of unfamiliar objects, much like humans and animals.

- Simulate physical interactions in a virtual environment before acting in the real world.

- Discover affordances — the actionable possibilities an object provides — without needing massive labeled datasets.

This biological analogy underpins our concept of Affordance Imagination: giving robots the ability to reason about function through simulation and exploration, the same way evolution equipped primates and humans with the ability to learn tools by trying them out.
<figure style="text-align: center;">
  <img src="resources/monkey-tool.png" alt="Motivation" width="500">
</figure>

## Introduction
This website presents the research outcomes of our group to demonstrate progress toward our funded project goal: using physical simulation to detect and reason about the affordances of objects.

Our central concept is affordance imagination — enabling robots to mentally simulate possible interactions with previously unseen objects. By integrating physics-based reasoning, geometric analysis, and learning methods (from demonstrations and large language models), our robots can classify novel objects, predict functional poses, and execute manipulation strategies without relying on massive amounts of training data.

The works presented here illustrate how affordance imagination bridges the gap between theory and practice: from seating a teddy bear on a previously unseen chair, to predicting hanging poses of tools, to capping containers, to leveraging LLMs for task decomposition. Together, these efforts chart a path toward safe, generalizable, and intelligent robot interaction in household and healthcare environments.

## Affordance Imagination

### Put a Lid on It! A Learning-Free Method to Cap a Container via Physical Simulations (UR 2025)
<div style="display: flex; align-items: center;"> <figure style="margin: 0; margin-right: 20px;"> <img src="resources/lid.png" alt="lid" width="300"> </figure> <p style="max-width: 500px;"> Develops a simulation-based method for matching unseen containers and lids. Uses Gaussian process distance fields and matching imagination to achieve over 91% success rate. <a href="https://arxiv.org/abs/2409.11831" target="_blank">Paper</a>. </p> </div>

### Goal-Guided Reinforcement Learning: Leveraging Large Language Models for Long-Horizon Task Decomposition (ICRA 2025)
<div style="display: flex; align-items: center;"> <figure style="margin: 0; margin-right: 20px;"> <img src="resources/g2rl.png" alt="g2rl" width="300"> </figure> <p style="max-width: 500px;"> Proposes G2RL, where LLMs generate subgoals to help reinforcement learning explore efficiently in long-horizon tasks. Validated across simulated environments with improved convergence. <a href="https://chirikjianlab.github.io/G2RL-LM/" target="_blank">Project Page</a>. </p> </div>


### RAIL: Robot Affordance Imagination with Large Language Models (ISER 2025)
<div style="display: flex; align-items: center;"> <figure style="margin: 0; margin-right: 20px;"> <img src="resources/rail.png" alt="rail" width="300"> </figure> <p style="max-width: 500px;"> Combines LLMs with physics-based simulation for automatic affordance reasoning. From minimal semantic input, robots classify novel objects, predict functional poses, and perform unseen tasks. <a href="https://arxiv.org/abs/2403.19369" target="_blank">Paper</a>. </p> </div>

### RaggeDi: Diffusion-based State Estimation of Disordered Rags, Sheets, Towels and Blankets (arXiv 2024)
<div style="display: flex; align-items: center;"> <figure style="margin: 0; margin-right: 20px;"> <img src="resources/raggedi.png" alt="raggedi" width="300"> </figure> <p style="max-width: 500px;"> Applies diffusion models for cloth state estimation. Represents cloth deformation as a translation map and achieves superior accuracy in both simulation and real-world experiments. <a href="https://arxiv.org/abs/2409.11831" target="_blank">Paper</a>. </p> </div>

### PRIMP: PRobabilistically-Informed Motion Primitives for Efficient Affordance Learning from Demonstration (T-RO 2024)
<div style="display: flex; align-items: center;"> <figure style="margin: 0; margin-right: 20px;"> <img src="resources/primp.png" alt="primp" width="300"> </figure> <p style="max-width: 500px;"> Introduces PRIMP, which learns probabilistic motion primitives from demonstrations and integrates them with workspace-aware motion planning (Workspace-STOMP). Demonstrated on tool-use and affordance-based tasks. <a href="https://doi.org/10.1109/TRO.2024.3390052" target="_blank">Paper</a>. </p> </div>

### Grasping by Hanging: A Learning-Free Grasping Detection Method for Previously Unseen Objects (arXiv 2024)
<div style="display: flex; align-items: center;"> <figure style="margin: 0; margin-right: 20px;"> <img src="resources/grasping-hanging.png" alt="grasping-hanging" width="300"> </figure> <p style="max-width: 500px;"> Introduces Grasping-by-Hanging (GbH), a learning-free approach where robots detect hangable structures to derive grasping poses. Particularly effective for thin or flat objects. <a href="https://arxiv.org/abs/2408.06734" target="_blank">Paper</a>. </p> </div>

### I Get the Hang of It! A Learning-Free Method to Predict Hanging Poses for Previously Unseen Objects (RA-L 2024)
<div style="display: flex; align-items: center;"> <figure style="margin: 0; margin-right: 20px;"> <img src="resources/hanging.png" alt="hanging" width="300"> </figure> <p style="max-width: 500px;"> Proposes a learning-free framework for predicting stable hanging poses using geometric and mechanical analysis. Outperforms learning-based baselines in simulation and real-world tests. <a href="https://arxiv.org/abs/2403.19369" target="_blank">Paper</a>. </p> </div>


### Prepare the Chair for the Bear! Robot Imagination of Sitting Affordance to Reorient Previously Unseen Chairs (RA-L 2023)
<div style="display: flex; align-items: center;">
  <figure style="margin: 0; margin-right: 20px;">
    <img src="resources/prepare-chair.png" alt="prepare-chair" width="300">
  </figure>
  <p style="max-width: 500px;">
    Robots reconstruct previously unseen chairs, simulate their sitting affordance, 
    and reorient them so a humanoid agent (teddy bear proxy) can be seated. 
    Demonstrates object classification and functional pose prediction via 
    physics-based imagination. <a href="https://github.com/ChirikjianLab" target="_blank">Code</a>.
  </p>
</div>

### Put the Bear on the Chair! Intelligent Robot Interaction with Previously Unseen Chairs via Robot Imagination (arXiv 2022)
<div style="display: flex; align-items: center;"> <figure style="margin: 0; margin-right: 20px;"> <img src="resources/bear-chair.png" alt="bear-chair" width="300"> </figure> <p style="max-width: 500px;"> Extends chair affordance reasoning by enabling a humanoid robot to physically seat a teddy bear. Introduces a human-assistance module to adjust inaccessible chair poses via natural language instructions. <a href="https://arxiv.org/abs/2108.05539" target="_blank">Paper</a>. </p> </div>
