#include <stdio.h>

typedef struct
{
    char name[50];
    int total_votes;
    int margin;
} Constituency;

void result(Constituency constituencies[], int totalConstituencies);
int calculateMargin(int a, int b);
void displayconstituency(Constituency constituencies[], int totalConstituencies);
void displayAllConstituencies(Constituency Constituencies[], int totalConstituencies);

int main()
{
    int totalConstituencies = 70;
    Constituency constituencies[] = {
        {"Narela", 87215, calculateMargin(87215, 78619)},
        {"Burari", 121181, calculateMargin(121181, 100580)},
        {"Timarpur", 55941, calculateMargin(55941, 54773)},
        {"Adarsh Nagar", 52510, calculateMargin(52510, 41028)},
        {"Badli", 61192, calculateMargin(61192, 46029)},
        {"Rithala", 104371, calculateMargin(104371, 74755)},
        {"Bawana", 119515, calculateMargin(119515, 88040)},
        {"Mundka", 89839, calculateMargin(89839, 79289)},
        {"Kirari", 105780, calculateMargin(105780, 83909)},
        {"Sultanpur Majra", 58767, calculateMargin(58767, 41641)},
        {"Nangloi Jat", 75272, calculateMargin(75272, 49021)},
        {"Mangolpuri", 62007, calculateMargin(62007, 55752)},
        {"Rohini", 70365, calculateMargin(70365, 32549)},
        {"Shalimar Bagh", 68200, calculateMargin(68200, 38605)},
        {"Shakur Basti", 56869, calculateMargin(56869, 35871)},
        {"Trinagar", 59073, calculateMargin(59073, 43177)},
        {"Wazirpur", 54721, calculateMargin(54721, 43296)},
        {"Model Town", 52108, calculateMargin(52108, 38693)},
        {"Sadar Bazar", 56177, calculateMargin(56177, 49870)},
        {"Chandni Chowk", 38993, calculateMargin(38993, 22421)},
        {"Matiamahal", 58120, calculateMargin(58120, 15396)},
        {"Ballimaran", 57004, calculateMargin(57004, 27181)},
        {"Karol Bagh", 52297, calculateMargin(52297, 44867)},
        {"Patel Nagar", 57512, calculateMargin(57512, 53463)},
        {"Moti Nagar", 57565, calculateMargin(57565, 45908)},
        {"Madipur", 52019, calculateMargin(52019, 41120)},
        {"Rajouri Garden", 64132, calculateMargin(64132, 45942)},
        {"Harinagar", 50179, calculateMargin(50179, 43547)},
        {"Tilak Nagar", 52134, calculateMargin(52134, 40478)},
        {"Janakpuri", 68986, calculateMargin(68986, 50220)},
        {"Vikaspuri", 135564, calculateMargin(135564, 122688)},
        {"Uttam Nagar", 103613, calculateMargin(103613, 73873)},
        {"Dwarka", 69137, calculateMargin(69137, 61308)},
        {"Matiala", 146295, calculateMargin(146295, 117572)},
        {"Najafgarh", 101708, calculateMargin(101708, 72699)},
        {"Bijwasan", 64951, calculateMargin(64951, 53675)},
        {"Palam", 82046, calculateMargin(82046, 73094)},
        {"Delhi Cantt", 22191, calculateMargin(22191, 20162)},
        {"Rajinder Nagar", 46671, calculateMargin(46671, 45440)},
        {"New Delhi", 30088, calculateMargin(30088, 25999)},
        {"Jangpura", 38859, calculateMargin(38859, 38184)},
        {"Kasturba Nagar", 38067, calculateMargin(38067, 27019)},
        {"Malviya Nagar", 39564, calculateMargin(39564, 37433)},
        {"R K Puram", 43260, calculateMargin(43260, 28807)},
        {"Mehrauli", 48349, calculateMargin(48349, 46567)},
        {"Chhatarpur", 80469, calculateMargin(80469, 74230)},
        {"Deoli", 86889, calculateMargin(86889, 50209)},
        {"Ambedkar Nagar", 46285, calculateMargin(46285, 42055)},
        {"Sangam Vihar", 54049, calculateMargin(54049, 53705)},
        {"Greater Kailash", 49594, calculateMargin(49594, 46406)},
        {"Kalkaji", 52154, calculateMargin(52154, 48633)},
        {"Tughlakabad", 62155, calculateMargin(62155, 47444)},
        {"Badarpur", 112991, calculateMargin(112991, 87103)},
        {"Okhla", 88943, calculateMargin(88943, 65304)},
        {"Trilokpuri", 58217, calculateMargin(58217, 57825)},
        {"Kondli", 61792, calculateMargin(61792, 55499)},
        {"Patparganj", 74060, calculateMargin(74060, 45988)},
        {"Laxmi Nagar", 65858, calculateMargin(65858, 54316)},
        {"Vishwas Nagar", 72141, calculateMargin(72141, 47099)},
        {"Krishnanagar", 75922, calculateMargin(75922, 56424)},
        {"Gandhinagar", 56858, calculateMargin(56858, 44110)},
        {"Shahdara", 62788, calculateMargin(62788, 57610)},
        {"Seemapuri", 66353, calculateMargin(66353, 55985)},
        {"Rohtas Nagar", 82896, calculateMargin(82896, 54994)},
        {"Seelampur", 79009, calculateMargin(79009, 36532)},
        {"Ghonda", 79987, calculateMargin(79987, 53929)},
        {"Babarpur", 76192, calculateMargin(76192, 57198)},
        {"Gokalpur", 80504, calculateMargin(80504, 72297)},
        {"Mustafabad", 85215, calculateMargin(85215, 67637)},
        {"Karawal Nagar", 107367, calculateMargin(107367, 84012)}};
    printf("\n----------Welcome to Delhi Assembly Elections Result(2025)----------");
    result(constituencies, totalConstituencies);

    return 0;
}

void displayconstituency(Constituency constituencies[], int totalConstituencies)
{
    int individualoption;

    while (1)
    {
        printf("\nEnter a consituency number ");
        if (scanf("%d", &individualoption) != 1 || individualoption < 0 || individualoption > totalConstituencies)
        {
            while (getchar() != '\n')
                ;
            continue;
        }
        if (individualoption == 0)
        {
            break;
        }
        else if (individualoption >= 1 && individualoption <= totalConstituencies)
        {
            printf("\n%s margin %d", constituencies[individualoption - 1].name, constituencies[individualoption - 1].margin);
        }
        else
        {
            printf("\nInvalid number");
        }
    }
}

void displayAllConstituencies(Constituency Constituencies[], int totalConstituencies)
{
    for (int i = 0; i < totalConstituencies; i++)
    {
        printf("\nMargin for %s: %d", Constituencies[i].name, Constituencies[i].margin);
    }
}

int calculateMargin(int a, int b)
{
    return a - b;
}

void result(Constituency constituencies[], int totalConstituencies)
{
    int option;
    while (1)
    {
        printf("\n\nEnter 1 for All | Enter 2 for Constituency-Wise | Enter 0 key to Exit: ");

        if (scanf("%d", &option) != 1 || option < 0 || option > 2)
        {
            while (getchar() != '\n')
                ; // clear input biffer
            continue;
        }

        if (option == 1)
        {
            displayAllConstituencies(constituencies, totalConstituencies);
        }
        else if (option == 2)
        {
            displayconstituency(constituencies, totalConstituencies);
        }
        else if (option == 0)
        {
            break;
        }
        else
        {
            printf("\nEnter valid option");
        }
    }
}