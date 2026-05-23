# ADR: Vision Node Refactor to Python 3 from C++

## Status
Undecided

## Timeline 
Dec. 5, 2019: ADR published

## Context
The focus of this ADR is the ROS vision node. Specifically, the programming language the node is based in. AUVic's software team is putting effort towards developing vision solutions for the sub, notably object detection and associated actions. There is a need to ensure a smooth transition and ensure that solutions are developed as soon as possible for testing, as it is a core functionality of the sub. Furthermore, there has been interest to assign new team members to efforts related to `OpenCV`.

## Decision 
A decision is proposed to fully refactor the vision node, including all its implementation in C++, to Python 3. The main motivation is the need to have a fully functioning vision node, with code that is easily unit testable and who’s syntax is easier to understand than C++. 
Specific motivations are listed:
-	As it is shown that Python and C++ functionality is interchangeable [1], and Python syntax is easier to understand, a preference exists to focus on higher level applications. 
- As opposed to employing the use of `CMakeLists.txt`, using Python only requires the Python interpreter itself [2]. As shown, nodes in Python with similar 
  functionality may be created with minimal dependencie on those files [3]
- A transition to Python as opposed to another scripting/programming language such as **Go, Rust, Java, or C** [4] is preferred as Python is a syntactically more preferable language for team members, and does not entail compile-time considerations.
- A transition to Python eliminates the risk of dealing with memory management and desctructors. The need for those features have not
  been determined at the time of this writing.
- A transition to Python will simplify the approach to writing automated unit tests, as syntax and lack of compile-time overhead 
  is minimized.
- The transition will provide us access to `numpy`, a computationally more efficient way of computing results. Furthermore, packages
  like `keras`, `theano` and `tensorflow` will lessen the barrier to entry for team members to develop deep learning solutions.

## Consequences 
Since any functionality in ROS with C++ may be also implemented in Python, minimal impact is expected. 
- As the vision node has no hardware dependency for the project, the refactor is expected to only be isolated to the node itself. 
- Since ROS abstracts the messages and services from the node’s implementation, no change is expected in other modes. 
- Although Python is a scripted language as opposed to C++, no major performance considerations are obvious at the time of this writing 
- Efforts towards writing automated tests will contain less overhead, and can be implemented with the `unittest` Python package.
- Certain efforts that were orignnally in C++ specific may be slowed, although that is not determined.
- If seen as a proof of concept for refactoring other nodes to Python, this isolated change will provide a basis for evaluating further refactoring

## Comments
_Relevant discussions and decisions may be recorded in this section for context_  

Robwasmann Dec 7, 2019:
Kinetic doesn't support Python 3.
Also, I'm worried about Python crashing in more unexpected ways. Since it's only compiled as it's interpreted, it won't catch errors until that particular part of the code (a particular function, say) gets executed. Personally I don't like languages like Python for anything serious where you need stability. We really don't want to vision node to crap out at an important moment. The 2018 Polaris vision code uses Python and it runs extremely slowly. 

Robwasmann Dec 9, 2019:
New members are always free to experiment with OpenCV in Python in the Vision testing repo, as well they can implement something first in Python and then convert it to C++

## Links
[1] https://www.theconstructsim.com/learn-ros-python-or-cpp/

[2] https://www.theconstructsim.com/infographic-start-ros-python-ros-cpp/

[3] https://github.com/ros/ros_tutorials

[4] http://wiki.ros.org/Client%20Libraries
