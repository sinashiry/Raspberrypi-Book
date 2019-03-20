//OpenCV HeaderFiles
#include <opencv2/opencv.hpp>
using namespace cv;

//C++ HeaderFiles
#include <stdio.h>
using namespace std;

int main()
{
	VideoCapture CAP(0);
	double fps = 30;
	Mat Buffer, Buffer_gray;
	while (true)
	{
		CAP >> Buffer;
		cvtColor(Buffer, Buffer_gray, CV_BGR2GRAY);
		GaussianBlur(Buffer_gray, Buffer_gray, Size(9, 9), 2, 2);
		vector<Vec3f> circles;
		HoughCircles(Buffer_gray, circles, CV_HOUGH_GRADIENT, 1, Buffer_gray.rows / 8, 200, 100, 0, 0);
		for (size_t i = 0; i < circles.size(); i++)
		{
			Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
			int radius = cvRound(circles[i][2]);
			circle(Buffer, center, 3, Scalar(0, 255, 0), -1, 8, 0);
			circle(Buffer, center, radius, Scalar(0, 0, 255), 3, 8, 0);
		}
		imshow("Circle Detection", Buffer);
		if (waitKey(1000 / fps) >= 0)
			break;
	}
	return 0;
}