import java.util.ArrayList;

public class InvSubByte {
	ArrayList<ArrayList<Integer>> SBOX = new ArrayList<ArrayList<Integer>>();
	int InversedByte;
	InvSubByte(int SubedByte){
		GenSbox();
		//System.out.println(SBOX);
		int row = 0;
		int column = 0;
		//System.out.println(SubedByte);
		OuterLoop:
		for (ArrayList<Integer> i : this.SBOX) {

			column = 0;
			for (Integer j : i) {
				//System.out.println(j == SubedByte);
				if (j == SubedByte) {						
					break OuterLoop;
				}
				column+=1;
					
					
					
			}
				
			row+=1;
		}
			
			
		
		//System.out.println(row);
		//System.out.println(column);
		this.InversedByte = (row*16)+column;
		
		
		
	}
	
	
	void GenSbox() {
		int k = 0;
		for (int i  = 0 ; i<16;i++) {
			ArrayList<Integer> row = new ArrayList<Integer>();
			
			for (int j  = 0 ; j<16;j++) {
				SubByte ByteN = new SubByte(k);
				row.add(ByteN.SubedByte);
				k+=1;
			}
			this.SBOX.add(row);
			
			}
			
		}
		
		
	}


