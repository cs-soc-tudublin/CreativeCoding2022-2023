#include <stdio.h>
#include <stdint.h>


#define BLACK 0xFF000000
#define WHITE 0xFFFFFFFF
#define RED   0xFF0000FF
#define GREEN 0xFF00FF00
#define BLUE  0xFFFF0000

#define WIDTH 500
#define HEIGHT 500


typedef uint32_t c32;


static c32 image[HEIGHT][WIDTH];

void rect(uint32_t, uint32_t, uint32_t, uint32_t, c32);
void square(uint32_t, uint32_t, uint32_t, c32);
void circle(uint32_t, uint32_t, uint32_t, c32);
void fillImage(c32);
void writeImage(const char *);

int main()
{
	for(uint32_t i  = 0; i < 10; i++)
		circle(i * 25,i * 30,i * 25, GREEN);
	rect(100,100,100,100,BLUE);
	writeImage("output.ppm");
	return 0;
}
void fillImage(c32 col)
{
	for(uint32_t i = 0; i < HEIGHT; i++)
		for(uint32_t ii = 0; ii < WIDTH; ii++)
			image[i][ii] = col;
}

void writeImage(const char * name)
{
	FILE * fp = fopen(name, "w+");
	fprintf(fp, "P6\n%d %d\n255\n", WIDTH, HEIGHT);

	for(uint32_t i = 0; i < HEIGHT; i++)
	{
		for(uint32_t ii = 0; ii < WIDTH; ii++)
		{
			c32 p = image[i][ii];
			uint8_t pixel[3] =  {
									(p & 0xFF0000FF) >> 0, //extract red
									(p & 0xFF00FF00) >> 8, //extract blue
									(p & 0xFFFF0000) >> 16  //extract green
								};
			fwrite(pixel, 1, 3, fp);
		}
	}
	fclose(fp);
	
}

void rect(uint32_t x, uint32_t y, uint32_t w, uint32_t h, c32 col)
{
	for(uint32_t i = y; i < y + h; i++)
		for(uint32_t ii = x; ii < x + w; ii++)
			image[i][ii] = col;
}

void square(uint32_t x, uint32_t y, uint32_t w, c32 col)
{
	rect(x, y, w, w, col);
}

void circle(uint32_t x, uint32_t y, uint32_t rad, c32 col)
{
	for(uint32_t i = y - rad; i < y + rad; i++)
	{
		for(uint32_t ii = x - rad; ii < x + rad; ii++)
		{
			uint32_t relX = i - x;
			uint32_t relY = ii - y;
			if((relX * relX) + (relY * relY) <= rad * rad)
				image[i][ii] = col;
		}
	}
}
