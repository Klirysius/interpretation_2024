#include <iostream>
#include <string>

template <typename T>
struct Node
{
    T data;
    Node *prev;
    Node *next;

    Node(const T &value) : data(value), prev(nullptr), next(nullptr) {}
};

template <typename T>
class DoublyLinkedList
{
private:
    Node<T> *head;
    Node<T> *tail;
    int size;

public:
    DoublyLinkedList() : head(nullptr), tail(nullptr), size(0) {}
    ~DoublyLinkedList() {}

    // Конструктор копирования
    DoublyLinkedList(const DoublyLinkedList &other)
    {
        head = nullptr;
        tail = nullptr;
        size = 0;

        Node<T> *temp = other.head;
        while (temp != nullptr)
        {
            push_back(temp->data);
            temp = temp->next;
        }
    }

    // Оператор присваивания
    DoublyLinkedList &operator=(const DoublyLinkedList &other)
    {
        if (this == &other)
        {
            return *this;
        }

        clear();

        Node<T> *temp = other.head;
        while (temp)
        {
            push_back(temp->data);
            temp = temp->next;
        }

        return *this;
    }

    void clear()
    {
        Node<T> *current = head;
        while (current)
        {
            Node<T> *next = current->next;
            delete current;
            current = next;
        }

        head = nullptr;
        size = 0;
    }
    void push_front(const T &);
    void push_back(const T &);
    void insert(int pos, const T &value);
    void shuffle();

    void remove(int index);

    bool isEmpty() const;

    int getSize() const;

    class Iterator
    {
    private:
        Node<T> *current;

    public:
        Iterator(Node<T> *ptr) : current(ptr) {}

        T &operator*()
        {
            return current->data;
        }

        bool operator!=(const Iterator &other)
        {
            return current != other.current;
        }

        Iterator &operator++()
        {
            current = current->next;
            return *this;
        }
    };

    Iterator begin()
    {
        return Iterator(head);
    }

    Iterator end()
    {
        return Iterator(nullptr);
    }
};

template <typename T>
void DoublyLinkedList<T>::push_front(const T &value)
{
    Node<T> *new_node = new Node<T>(value);

    if (head == nullptr)
    {
        head = tail = new_node;
    }
    else
    {
        new_node->next = head;
        head->prev = new_node;
        head = new_node;
    }

    size++;
}

template <typename T>
void DoublyLinkedList<T>::push_back(const T &value)
{
    Node<T> *new_node = new Node<T>(value);

    if (tail == nullptr)
    {
        head = tail = new_node;
    }
    else
    {
        new_node->prev = tail;
        tail->next = new_node;
        tail = new_node;
    }

    size++;
}

template <typename T>
void DoublyLinkedList<T>::insert(int pos, const T &value)
{
    if (pos < 0 || pos > size)
    {
        throw std::range_error("Out of range");
    }
    if (pos == 0)
    {
        push_front(value);
    }
    else if (pos == size)
    {
        push_back(value);
    }
    else
    {
        Node<T> *current = head;
        for (int i = 0; i < pos; i++)
        {
            current = current->next;
        }

        Node<T> *new_node = new Node<T>(value);
        new_node->prev = current->prev;
        new_node->next = current;
        current->prev->next = new_node;
        current->prev = new_node;

        size++;
    }
}

template <typename T>
void DoublyLinkedList<T>::remove(int index)
{
    if (index < 0 || index >= size)
    {
        throw std::range_error("Out of range");
    }
    Node<T> *current = head;
    for (int i = 0; i < index; i++)
    {
        current = current->next;
    }
    if (current->prev)
    {
        current->prev->next = current->next;
    }
    else
    {
        head = current->next;
    }
    if (current->next)
    {
        current->next->prev = current->prev;
    }
    else
    {
        tail = current->prev;
    }
    delete current;
    size--;
}
template <typename T>
bool DoublyLinkedList<T>::isEmpty() const
{
    return size == 0;
}

template <typename T>
int DoublyLinkedList<T>::getSize() const
{
    return size;
}

int main()
{
    DoublyLinkedList<int> list1;
    DoublyLinkedList<int> list2;
    list1.push_back(1);
    list1.push_back(2);

    std::cout << "Первый список:\n";
    for (auto el : list1)
    {
        std::cout << el << " ";
    }

    std::cout << "\nВторой список:\n";
    list2 = list1;
    for (auto el : list2)
    {
        std::cout << el << " ";
    }

    DoublyLinkedList<int> list3(list1);

    std::cout << "\nТретий список:\n";
    for (auto el : list3)
    {
        std::cout << el << " ";
    }

    DoublyLinkedList<int> list4;
    list4 = list1;
    list1.insert(2,1);
    std::cout << "\nЧетвёртый список:\n";
    for (auto el : list4)
    {
        std::cout << el << " ";
    }

    std::cout << "\nПервый список:\n";
    for (auto el : list1)
    {
        std::cout << el << " ";
    }
    return 1;
}