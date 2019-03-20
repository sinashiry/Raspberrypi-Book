//OpenCV Header Files
#include <opencv2/opencv.hpp>
using namespace cv;

int main()
{
	VideoCapture CAP(0);
	int fps = 30;
	Mat Buffer;
	while (true)
	{
		CAP >> Buffer;
		imshow("OUT", Buffer);
		if (waitKey(1000 / fps) >= 0)
			break;
	}
	CAP.release();
	return 0;
}