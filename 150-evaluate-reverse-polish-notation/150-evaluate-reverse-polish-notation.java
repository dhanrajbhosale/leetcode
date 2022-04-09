class Solution {

    public int evalRPN(String[] tokens) {

        Stack<Integer> st=new Stack<Integer>();
        
        for(int i=0;i<tokens.length;i++){
            String c=tokens[i];
              try{
                   st.push(Integer.parseInt(c));
              }   catch(Exception e){
                  int op2=st.pop();
                int op1=st.pop();
               
                switch(c)
                {
                        case "+":st.push(op1+op2);break;
                        case "-":st.push(op1-op2);break;
                        case "*":st.push(op1*op2);break;
                        case "/":st.push(op1/op2);break;
                }
              }       
            
        }  
        return st.pop();
    }
}