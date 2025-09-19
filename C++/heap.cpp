#include<bits/stdc++.h>
using namespace std;

class Heap {
    private:
    vector<int> heap;

    int leftchild(int index)
    {
        return 2 * index + 1;
    }

    int rightchild(int index)
    {
        return 2 * index + 2;
    }

    int parent( int index )
    {
        return (index - 1) / 2;
    }

    void swap(int index1, int index2)
    {
        int temp = heap[index1];
        heap[index1] = heap[index2];
        heap[index2] = temp;
    }

    

    public:
    void printHeap()
    {
        cout << "\n[";
        for (size_t i = 0; i< heap.size(); i++)
        {
            cout << heap[i];
            if ( i < heap.size() - 1)
            {
                cout << ", ";
            }
        }
        cout << "]\n";
    }

    void insert(int value)
    {
        heap.push_back(value);
        int current = heap.size() - 1;

        while (current > 0 && heap[current] > heap[parent(current)])
        {
            swap(current, parent(current));
            current = parent(current);
        }
    }

    void sinkDown(int index)
    {
        int maxIndex = index;
        while (true)
        {
            int leftIndex = leftchild(index);
            int rightIndex = rightchild(index);

            if (leftIndex < heap.size() && heap[leftIndex] > heap[maxIndex])
            {
                maxIndex = leftIndex;
            }

            if (rightIndex < heap.size() && heap[rightIndex] > heap[maxIndex])
            {
                maxIndex = rightIndex;
            }

            if (maxIndex != index)
            {
                swap(index, maxIndex);
                index = maxIndex;
            }else{
                return;
            }
        }
    }
    

    int remove()
    {
        if (heap.empty())
        {
            return INT_MIN;
        }

        int maxValue = heap.front();

        if (heap.size() == 1)
        {
            heap.pop_back();
        }
        else
        {
            heap[0] = heap.back();
            heap.pop_back();
            sinkDown(0);
        }
        return maxValue;
    }
};

int main()
{
    Heap* heap = new Heap();
    heap->insert(95);
    heap->insert(75);
    heap->insert(80);
    heap->insert(55);
    heap->insert(60);
    heap->insert(50);
    heap->insert(65);
    
    heap->printHeap();

    heap->remove();

    heap->printHeap();

    heap->remove();

    heap->printHeap();
}