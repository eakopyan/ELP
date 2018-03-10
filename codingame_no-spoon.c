int main()
{
    int width; // the number of cells on the X axis
    scanf("%d", &width);
    int height; // the number of cells on the Y axis
    scanf("%d", &height); fgetc(stdin);
    
    int x1, y1, x2, y2, x3, y3;
    int nextr, nextb;
    char *tab[height];
    
    for (int a = 0; a < height; a++) {
        char line[32]; // width characters, each either 0 or .
        fgets(line, 32, stdin); // width characters, each either 0 or .
        tab[a] = malloc(sizeof(char) * (strlen(line) + 1));
        strcpy(tab[a], line);
    }
    
    for(int i = 0; i<height; i++) {
        for (int j = 0; j<strlen(tab[i]); j++) {
            switch(tab[i][j]) {
                case '.' : // empty cell
                break;
                
                case '0' : // power cell
                x1 = j;
                y1 = i;
                nextr = 1;
                nextb = 1;
                if((j==strlen(tab[i])-1)||(tab[i][j+1] != '0')) { // out of range or empty cell on the right
                    while(j<strlen(tab[i])) {
                        if(tab[i][j+1] != '0') j++;
                        
                    }
                    x2 = -1;
                    y2 = -1;
                } else { // power cell on the right
                    x2 = j+1;
                    y2 = i;
                }
                if((i==height-1)||(tab[i+1][j] != '0')) { // out of range or empty cell below
                    x3 = -1;
                    y3 = -1;
                } else { // power cell below
                    x3 = j;
                    y3 = i+1;
                }
                printf("%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, y3);
            }
        }
    }

    return 0;
}
