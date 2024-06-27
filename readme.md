# Using Web APIs in Python

These materials are designed to power a 4-session (2 hours each) class about Web APIs and using Python to access them. The course is designed to be led by an instructor, but many of the walkthroughs and exercises are appropriate for self study.

## For Instructors:

* Files are named to indicate the order in which they should be delivered. 
* Any markdown files are lecture notes, written with the expectation that you'll have a (digital) blackboard available where you can illustrate many of the concepts in the lecture.
    * If you won't have that, you may wish to create some diagrams or slides to accompany the lesson plans.
* Any Python files are designed with the expectation that you step through them with a debugger and explain the code as you do so.
* Periodically there are "micro" and "mini" exercises embedded in the markdown and Python files.
    * Micro exercises should take about 1-2 minutes to complete.
    * Mini exercises should take about 5 minutes to complete. 
* Each lesson contains an exercise and a solution to the exercise.
    * Exercises are designed with the expectation that students work on them for about an hour.
    * An hour may not actually be enough time to finish, especially any tasks labeled "bonus"

## Dependencies / Configuration

This class relies heavily on the [requests](https://requests.readthedocs.io/en/latest/) module and some of the bonus work uses [OpenAI's Python library](https://github.com/openai/openai-python). For a more detailed writeup on how to use `venv` and properly manage your libraries see our detailed instructions in this file [/01-package-management-web-requests/02-venv-dependency-management.md](/01-package-management-web-requests/02-venv-dependency-management.md). 

If you already know about all that, then all you need is:

```
pip install requests openai
```

## Support Teb's Lab

These materials were created by [Tyler Bettilyon](https://www.linkedin.com/in/tylerbettilyon/) and [Teb's Lab](https://tebs-lab.com). You can support the creation of more free, open source, public domain educational materials by sharing them with others [subscribing to our newsletter](http://blog.tebs-lab.com), or signing your team up for one of our [corporate training classes](https://www.tebs-lab.com/course-catalog), or signing yourself up for one of our [open enrollment classes](https://www.tebs-lab.com/upcoming-classes) (when available).