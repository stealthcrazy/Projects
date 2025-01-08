import java.util.ArrayList;

public class Opperations {
	
	static ArrayList<ArrayList<Integer>> AddRoundKEY(State Array1 , State Array2){
		ArrayList<ArrayList<Integer>> newArray = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> rowNewArray_1 = new ArrayList<Integer>();
		ArrayList<Integer> rowNewArray_2 = new ArrayList<Integer>();
		ArrayList<Integer> rowNewArray_3 = new ArrayList<Integer>();
		ArrayList<Integer> rowNewArray_4 = new ArrayList<Integer>();
		
		for(int i = 0 ; i<Array1.stateArray2D.size();++i) {
			for(int j = 0 ; j<Array1.stateArray2D.get(i).size();++j) {
				int XorVal = (int) (Array1.stateArray2D.get(i).get(j) ^ Array2.stateArray2D.get(i).get(j));
				
				if(i == 0) {
					rowNewArray_1.add(XorVal);
				}else if( i == 1) {
					rowNewArray_2.add(XorVal);
				}else if(i == 2) {
					rowNewArray_3.add(XorVal);
				}else if(i == 3) {
					rowNewArray_4.add(XorVal);
				}
				
	
			}
		}
		
		newArray.add(rowNewArray_1);
		newArray.add(rowNewArray_2);
		newArray.add(rowNewArray_3);
		newArray.add(rowNewArray_4);
		
		return newArray ;
		
	}
	static ArrayList<ArrayList<Integer>> InvAddRoundKEY(State Array1 , State Array2){
		ArrayList<ArrayList<Integer>> newArray = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> rowNewArray_1 = new ArrayList<Integer>();
		ArrayList<Integer> rowNewArray_2 = new ArrayList<Integer>();
		ArrayList<Integer> rowNewArray_3 = new ArrayList<Integer>();
		ArrayList<Integer> rowNewArray_4 = new ArrayList<Integer>();
		
		for(int i = Array1.stateArray2D.size()-1 ; i>=0;--i) {
			for(int j = 0 ; j<Array1.stateArray2D.get(i).size();++j) {
				int XorVal = (int) (Array1.stateArray2D.get(i).get(j) ^ Array2.stateArray2D.get(i).get(j));
				
				if(i == 0) {
					rowNewArray_1.add(XorVal);
				}else if( i == 1) {
					rowNewArray_2.add(XorVal);
				}else if(i == 2) {
					rowNewArray_3.add(XorVal);
				}else if(i == 3) {
					rowNewArray_4.add(XorVal);
				}
				
	
			}
		}
		
		newArray.add(rowNewArray_1);
		newArray.add(rowNewArray_2);
		newArray.add(rowNewArray_3);
		newArray.add(rowNewArray_4);
		
		return newArray ;
		
	}
	
	
	static ArrayList<ArrayList<Integer>> SubIntegers(State Array2D) {
		ArrayList<ArrayList<Integer>> newArray = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> rowNewArray_1 = new ArrayList<Integer>();
		ArrayList<Integer> rowNewArray_2 = new ArrayList<Integer>();
		ArrayList<Integer> rowNewArray_3 = new ArrayList<Integer>();
		ArrayList<Integer> rowNewArray_4 = new ArrayList<Integer>();
		
		for(int i = 0 ; i<Array2D.stateArray2D.size();++i) {
			for(int j = 0 ; j<Array2D.stateArray2D.get(i).size();++j) {
				int x = (int) Array2D.stateArray2D.get(i).get(j);
				SubByte Sub = new SubByte(x);
				
				if(i == 0) {
					rowNewArray_1.add((int) Sub.SubedByte);
				}else if( i == 1) {
					rowNewArray_2.add((int) Sub.SubedByte);
				}else if(i == 2) {
					rowNewArray_3.add((int) Sub.SubedByte);
				}else if(i == 3) {
					rowNewArray_4.add((int) Sub.SubedByte);
				}
				
				
			}
		
		
		
		}
		newArray.add(rowNewArray_1);
		newArray.add(rowNewArray_2);
		newArray.add(rowNewArray_3);
		newArray.add(rowNewArray_4);
		
		return newArray ;
		
	}
	static ArrayList<ArrayList<Integer>> InvSubIntegers(State Array2D) {
		ArrayList<ArrayList<Integer>> newArray = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> rowNewArray_1 = new ArrayList<Integer>();
		ArrayList<Integer> rowNewArray_2 = new ArrayList<Integer>();
		ArrayList<Integer> rowNewArray_3 = new ArrayList<Integer>();
		ArrayList<Integer> rowNewArray_4 = new ArrayList<Integer>();
		
		for(int i = 0 ; i<Array2D.stateArray2D.size();++i) {
			for(int j = 0 ; j<Array2D.stateArray2D.get(i).size();++j) {
				int x = (int) Array2D.stateArray2D.get(i).get(j);
				InvSubByte InvSub = new InvSubByte(x);
				
				if(i == 0) {
					rowNewArray_1.add((int) InvSub.InversedByte);
				}else if( i == 1) {
					rowNewArray_2.add((int) InvSub.InversedByte);
				}else if(i == 2) {
					rowNewArray_3.add((int) InvSub.InversedByte);
				}else if(i == 3) {
					rowNewArray_4.add((int) InvSub.InversedByte);
				}
				
				
			}
		
		
		
		}
		newArray.add(rowNewArray_1);
		newArray.add(rowNewArray_2);
		newArray.add(rowNewArray_3);
		newArray.add(rowNewArray_4);
		
		return newArray ;
		
	}
	
	static ArrayList<ArrayList<Integer>> copyArray(State array){
		ArrayList<ArrayList<Integer>> duplicate = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> rowArray2D_1 = new ArrayList<Integer>();
		ArrayList<Integer> rowArray2D_2 = new ArrayList<Integer>();
		ArrayList<Integer> rowArray2D_3 = new ArrayList<Integer>();
		ArrayList<Integer> rowArray2D_4 = new ArrayList<Integer>();
		for(int i = 0 ; i < 4 ;++i ) {
					
			rowArray2D_1.add(array.stateArray2D.get(0).get(i));

		}
		for(int i = 0 ; i < 4 ;++i ) {
			
			rowArray2D_2.add(array.stateArray2D.get(1).get(i));

		}
		for(int i = 0 ; i < 4 ;++i ) {
			
			rowArray2D_3.add(array.stateArray2D.get(2).get(i));

		}
		for(int i = 0 ; i < 4 ;++i ) {
			
			rowArray2D_4.add(array.stateArray2D.get(3).get(i));

		}
		duplicate.add(rowArray2D_1);
		duplicate.add(rowArray2D_2);
		duplicate.add(rowArray2D_3);
		duplicate.add(rowArray2D_4);
		
		
		return duplicate;
		
	}
	static int selfXorBits(int[] array) {
		int temp = array[0] ;
		
		for(int i = 1 ; i<8 ;++i) {
			//System.out.print(temp);
			//System.out.print(i);
			
			//System.out.print(" "+array[i]+" =");
			
			temp ^=array[i];
			//System.out.print(temp+"\n");
			
			
			
		}
		return temp;
	}
	static int selfXorBits(int[] array,int size) {
		int temp = array[0] ;
		
		for(int i = 1 ; i<size ;++i) {
			//System.out.print(i + " :");
			//System.out.print(temp);
			
			
			//System.out.print(" "+array[i]+" =");
			
			temp ^=array[i];
			//System.out.print(temp+"\n");
			
			
			
		}
		//System.out.print("\n");
		//System.out.print("\n");
		return temp;
	}
	
	
	static ArrayList<Integer>  extractColumn(int coulmnNumber, ArrayList<ArrayList<Integer>> array ) {
		ArrayList<Integer>  Coulmn = new ArrayList<Integer>();
		for(int i = 0 ; i<array.size();++i) {
			Coulmn.add(array.get(i).get(coulmnNumber));
		}
		
		return Coulmn;
		
		
		
	}
	
	
	
	
}
