import java.nio.charset.StandardCharsets;
import java.util.ArrayList;

public class State {
	
	int[] stateArray;
	ArrayList<ArrayList<Integer>> stateArray2D;

	
	
	
	State(String input){
		this.stateArray = getIntegers(input);
		this.stateArray2D = formatArray(stateArray);
		
	}
	
	State(ArrayList<ArrayList<Integer>> Array){
		this.stateArray2D = Array;
	}
	
	State(int[] intArray){
		this.stateArray = intArray;
		this.stateArray2D = formatArray(stateArray);
	}
	
	
	int[] getIntegers(String input) {
		
		/*
		byte[] array = input.getBytes(StandardCharsets.UTF_8);
		//System.out.println(array.length);
		for(int i = 0 ; i<array.length;++i) {
			//System.out.println(i);
			Iarray[i] = array[i];
		}*/
		int[] intArray = new int[16];
		int index = 0;
        for (char c : input.toCharArray()) {
            int intValue = (int) c;
            String hexValue = Integer.toHexString(intValue);
            
            // Ensure that the hex value is always 2 digits long
            if (hexValue.length() < 2) {
                hexValue = "0" + hexValue;
            }
            
            // Convert each 2-digit hex value back to integer and store in the array
            for (int i = 0; i < hexValue.length(); i += 2) {
                intArray[index++] = Integer.parseInt(hexValue.substring(i, i + 2), 16);
            }
        }
		return intArray;
		
	}
	
	ArrayList<ArrayList<Integer>> formatArray(int[] array){
		ArrayList<ArrayList<Integer>> array2D = new ArrayList<ArrayList<Integer>>() ; 
		ArrayList<Integer> rowArray2D_1 = new ArrayList<Integer>();
		ArrayList<Integer> rowArray2D_2 = new ArrayList<Integer>();
		ArrayList<Integer> rowArray2D_3 = new ArrayList<Integer>();
		ArrayList<Integer> rowArray2D_4 = new ArrayList<Integer>();
		
		
		int counter = 0 ;
		
		
		for(int i = 0 ; i < 4 ;++i ) {
			
			rowArray2D_1.add(array[counter]);
			rowArray2D_2.add(array[counter+1]);
			rowArray2D_3.add(array[counter+2]);
			rowArray2D_4.add(array[counter+3]);
			counter+=4;
			
			
			
			
		}
		array2D.add(rowArray2D_1);
		array2D.add(rowArray2D_2);
		array2D.add(rowArray2D_3);
		array2D.add(rowArray2D_4);
		
		
		return array2D;
		
	}
	
	
	public String toString() {
		String displayString = "";
		
		for(int i = 0 ; i< this.stateArray2D.size(); ++i) {
			displayString += "[";
			for(int j = 0 ; j< this.stateArray2D.size(); ++j) {
				displayString += Integer.toHexString(this.stateArray2D.get(i).get(j)) + "  " ;
			}
			displayString += "] \n";
		}
		return displayString;
		
		
	}
	public static String toString(ArrayList<ArrayList<Integer>> Array) {
		String displayString = "";
		
		for(int i = 0 ; i< Array.size(); ++i) {
			displayString += "[";
			for(int j = 0 ; j< Array.size(); ++j) {
				displayString += Integer.toHexString(Array.get(i).get(j)) + "  " ;
			}
			displayString += "] \n";
		}
		return displayString;
		
		
	}
	String display(){
		String array = "[ ";
		
		for(int i = 0 ; i<this.stateArray.length ;++i) {
			array += this.stateArray[i] + " ";
			
		}
		array+="]";
		return array;
		
		
	}
	
	
	
	

}
