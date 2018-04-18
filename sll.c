#include<stdio.h>
#include<stdlib.h>
typedef struct node
{
  int data;
  struct node* next;
}node;

node* list=NULL;

node* createl()
{
  int i,d[5]={1,2,3,5,6};
  node* temp,*newnode;
  for(i=0;i<3;i++)
  {
    newnode=(node*)malloc(sizeof(node));
    newnode->data=d[i];
    newnode->next=NULL;
    if(list==NULL)
    {
      list=newnode;
      temp=newnode;
    }
    else
    {
      temp->next=newnode;
      temp=newnode;
    }
  }
  return list;
}


void display(node* list)
{
  node* temp;
  temp=list;
  printf("LInked list is as follows:\n");
  while(temp!=NULL)
  {
    printf("%d\t",temp->data);
    temp=temp->next;
  }
  printf("\n");
}


node* insertatbeg(node* list,int val)
{
  node* newnode;
  newnode=(node*)malloc(sizeof(node));
  newnode->data=val;
  newnode->next=list;
  list=newnode;
  return(list);
}

node* insertatlast(node* list,int val)
{
  node* newnode,*temp;
  newnode=(node*)malloc(sizeof(node));
  newnode->data=val;
  newnode->next=NULL;
  temp=list;
  while(temp->next!=NULL)
  {
    temp=temp->next;
  }
  temp->next=newnode;
  return(list);
}

node* deleteatbeg(node* list)
{
  node* temp;
  temp=list;
  list=temp->next;
  free(temp);
  return(list);
}

node* deleteatlast(node* list)
{
  node* temp,*temp1;
  temp=list;
  temp1=list;
  while(temp->next!=NULL)
  {
    temp1=temp;
    temp=temp->next;
  }
  temp1->next=NULL;
  free(temp);
  return(list);
}

void main()
{
    node* list=createl();
    display(list);
    list=insertatbeg(list,0);
    printf("After inserting at begining ll became:\n");
    display(list);
    list=insertatlast(list,4);
    printf("After inserting at last ll became:\n");
    display(list);
    list=deleteatbeg(list);
    printf("After deleting an element from begining ll became:\n"); 
    display(list);
}
