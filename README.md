# How-to-win-automatically-at-beer-pong-
A project combining object detection and a bit of maths/physics

At first, I created a informatic model of the problem and solve it:
  1. Developing an algorithm that generate a movement simulation according to the physical equation
  2. Then I create a created a program that by using pixel change in the differents image return me a trajectory by using interpolation polynomials
  3. Creation of a python module with the help of OPENMV to control differents modules (camera, motors)

Then I implement all of this into reality:
  4. Algorithm that from pixel difference determine brithness for background subtracting
  5. Motor equation solver for a control of the movement with precision.

Finally, I face reality: python is to slow for this, but a solution to this may be Cython (not learned properly yet)

Next objectif:
  Develop a machine learning algorithm do accelerate the image processing

    Thanks you for your time
    Clement Yahia-Ama
