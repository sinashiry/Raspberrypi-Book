//OpenCV Header Files
#include <opencv2/opencv.hpp>
using namespace cv;

int main()
{
	VideoCapture CAP(0);
	int fps = 30;
	Mat Buffer_Old, Buffer_New, Buffer_New_GRAY, Buffer_Old_GRAY,Difference;
	CAP >> Buffer_Old;
	while (true)
	{
		CAP >> Buffer_New;
		Difference = Buffer_New - Buffer_Old;
		Buffer_New.copyTo(Buffer_Old);
		Vec3b Pixel;
		int min_row, min_col, max_row, max_col;
		min_row=min_col=max_row=max_col=-1;
		for (int i = 0; i < 640; i++)
		{
			for (int j = 0; j < 480; j++)
			{
				 Pixel=Difference.at<Vec3b>(Point(i, j));
				 if (Pixel[0] > 200 && Pixel[1] > 200 && Pixel[2] >200)
				 {
					 if (min_row==-1)
						 min_row = i;
					 if (min_col==-1)
						 min_col = j;
					 if (min_row>i)
						 min_row = i;
					 if (max_row<i)
						 max_row = i;
					 if (min_col>j)
						 min_col = j;
					 if (max_col<j)
						 max_col = j;
				 }
			}
		}
		rectangle(Buffer_New, Point(min_row, min_col), Point(max_row, max_col), Scalar(0, 255, 0), 3);
		imshow("Motions", Buffer_New);
		if (waitKey(1000 / fps) >= 0)
			break;
	}
	CAP.release();
}