#include <stdio.h>
using namespace std;

#include <opencv2/opencv.hpp>
using namespace cv;

int main()
{
	vector<Rect> faces;
	CascadeClassifier face_cascade;
	String face_cascade_name = "C:\\opencv-3.0.0.\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_alt.xml";
	face_cascade.load(face_cascade_name);
	int face_size = 10;
	double scalar_factor = 3;
	int min_neighbours = 2;
	VideoCapture cap(0);
	UMat frame, frameGray;
	Rect r;
	while (true)
	{
		cap >> frame;
		cvtColor(frame, frameGray, COLOR_BGR2GRAY);
		equalizeHist(frameGray, frameGray);
		face_cascade.detectMultiScale(frameGray, faces, scalar_factor,
			                          min_neighbours, 0 | CASCADE_SCALE_IMAGE,
									  Size(face_size, face_size));
		for (int f = 0; f < faces.size(); f++)
		{
			r = faces[f];
			rectangle(frame, Point(r.x, r.y), 
				      Point(r.x + r.width, r.y + r.height),
					  Scalar(0, 255, 0), 3);
		}
		imshow("Video Capture", frame);
		if (waitKey(1) == 27) break;
	}
	cap.release();
	return 0;
}