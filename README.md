### Timelapse and mosaic videos

This project is a project that will allow you to perform switch back and forth between a timelapse and mosaic video.

## Required libraries

In order to use this UI, you will need to download some libraries.

# Install Homebrew on Mac OS

To install homebrew, run the following command then follow the instruction:

```terminal
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

then, after the installation, run :

```terminal
brew doctor
```

# Install OpenCV

Make sure to install OpenCV 3.0 or newer

**Installation under Mac OS**

You will need to install OpenCV with contrib:
To do so, download the source code as follows:
terminal
```
git clone https://github.com/Itseez/opencv.git
git clone https://github.com/Itseez/opencv_contrib
```

To install, run the following command:

```terminal
cd opencv
mkdir build && cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules ..
make -j8
sudo make install
```

If you are unable to install it, follow this guide:
https://blogs.wcode.org/2014/10/howto-install-build-and-use-opencv-macosx-10-10/

and setting OPENCV_EXTRA_MODULES_PATH to `<path/to/opencv_contrib/modules>` in cmake gui.

**Installation under Linux**

OpenCV requires some packages to be installed for it to work under Linux, you will need to run:

```terminal
sudo apt-get install build-essential
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
```

Then, download the source code as follows:

```terminal
git clone https://github.com/Itseez/opencv.git
git clone https://github.com/Itseez/opencv_contrib.git
```

To compile and install run:

```terminal
cd opencv
mkdir build && cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules ..
make -j8
sudo make install
```

# Main Project

Once the libraries have been download and installed, you are now able to run the project:

To run the timelapse stabilization algorithm on a video or an already existing timelapse, simply run:

```terminal
python stabilize_film.py <path/to/film>
```

To run the timelapse stabilization algorithm on a video and create a timelapse video from it, simply run:
On the other hand, if you want to create a timelapse and stablize it without, please run:

```terminal
python stabilize_film.py <path/to/film> true
```

## Mosaic

The mosaic aspect is yet to be implemented and will be just a side project that will be implemented in the near future
