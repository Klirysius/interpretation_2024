#include <iostream>

using namespace std;

class Test{

    private:
        int sum = 0;
    
    public:
    Test(int a, int b){
        sum += a + b;
    }

    Test(string a, string  b){
        sum += a.length() + b.length();
    }

    int get_sum(){
        return sum;
    }

    string param = "PUBLIC";
};

int main(){
    Test test1(1, 2); // Передача двух целых чисел
    cout << test1.get_sum() << endl;

    Test test2("123", "12"); // Передача двух строк
    cout << test2.get_sum() << endl;
    // test2.sum Нельзя напрямую получить доступ к полю
    cout << test2.param;
    return 1;
}