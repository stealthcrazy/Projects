import java.util.ArrayList;

public class MixColumns {

	
	
	
	static ArrayList<ArrayList<Integer>>  MixColumn(State array) {
		
		ArrayList<ArrayList<Integer>> arrayDuplicate = Opperations.copyArray(array);
		ArrayList<ArrayList<Integer>> mixedArray = new ArrayList<ArrayList<Integer>>() ;
		ArrayList<Integer> rowArray2D_1 = new ArrayList<Integer>();
		ArrayList<Integer> rowArray2D_2 = new ArrayList<Integer>();
		ArrayList<Integer> rowArray2D_3 = new ArrayList<Integer>();
		ArrayList<Integer> rowArray2D_4 = new ArrayList<Integer>();
		
		final int[][] Matrix = {
			    { 2, 3, 1, 1 },
			    { 1, 2, 3, 1 },
			    { 1, 1, 2, 3 },
			    { 3, 1, 1, 2 }
			};
		
		for(int k =0 ;k< arrayDuplicate.size();++k ) {
			ArrayList<Integer> Column =  Opperations.extractColumn(k,arrayDuplicate);
			ArrayList<Integer> newColumn =  new ArrayList<Integer>() ;
			
			for(int i =0 ;i< Column.size();++i) {
				int[] products = new int[4];
				for(int j =0 ;j< Column.size();++j ) {
					products[j] = GF_Multiply(Column.get(j),Matrix[i][j] );
				}
				newColumn.add(Opperations.selfXorBits(products,4));
			}
			rowArray2D_1.add(newColumn.get(0));
			rowArray2D_2.add(newColumn.get(1));
			rowArray2D_3.add(newColumn.get(2));
			rowArray2D_4.add(newColumn.get(3));
		}
		mixedArray.add(rowArray2D_1);
		mixedArray.add(rowArray2D_2);
		mixedArray.add(rowArray2D_3);
		mixedArray.add(rowArray2D_4);
		
		
		return mixedArray;
		
	}
	static ArrayList<ArrayList<Integer>>  InvMixColumn(State array) {
		
		ArrayList<ArrayList<Integer>> arrayDuplicate = Opperations.copyArray(array);
		ArrayList<ArrayList<Integer>> mixedArray = new ArrayList<ArrayList<Integer>>() ;
		ArrayList<Integer> rowArray2D_1 = new ArrayList<Integer>();
		ArrayList<Integer> rowArray2D_2 = new ArrayList<Integer>();
		ArrayList<Integer> rowArray2D_3 = new ArrayList<Integer>();
		ArrayList<Integer> rowArray2D_4 = new ArrayList<Integer>();
		
		final int[][] Matrix = {
			    { 0x0e, 0x0b, 0x0d, 0x09 },
			    { 0x09, 0x0e, 0x0b, 0x0d },
			    { 0x0d, 0x09, 0x0e, 0x0b },
			    { 0x0b, 0x0d, 0x09, 0x0e }
			};
		
		for(int k =0 ;k< arrayDuplicate.size();++k ) {
			ArrayList<Integer> Column =  Opperations.extractColumn(k,arrayDuplicate);
			ArrayList<Integer> newColumn =  new ArrayList<Integer>() ;
			
			for(int i =0 ;i< Column.size();++i) {
				int[] products = new int[4];
				for(int j =0 ;j< Column.size();++j ) {
					products[j] = Inv_GF_Multiply(Column.get(j),Matrix[i][j] );
				}
				newColumn.add(Opperations.selfXorBits(products,4));
			}
			rowArray2D_1.add(newColumn.get(0));
			rowArray2D_2.add(newColumn.get(1));
			rowArray2D_3.add(newColumn.get(2));
			rowArray2D_4.add(newColumn.get(3));
		}
		mixedArray.add(rowArray2D_1);
		mixedArray.add(rowArray2D_2);
		mixedArray.add(rowArray2D_3);
		mixedArray.add(rowArray2D_4);
		
		
		return mixedArray;
		
	}
	
	
	
	/*
	static int[] test(int[] column) {
		final int[][] Matrix = {
			    { 2, 3, 1, 1 },
			    { 1, 2, 3, 1 },
			    { 1, 1, 2, 3 },
			    { 3, 1, 1, 2 }
			};
		int[] result = new int[4];
		for(int i =0 ;i< 4;++i) {
			int[] products = new int[4];
			for(int j =0 ;j< 4;++j ) {
				products[j] = GF_Multiply(column[j],Matrix[i][j] );
				
				
			}
			System.out.println(Integer.toHexString(products[0]) + " " + Integer.toHexString(products[1]) + " " + Integer.toHexString(products[2]) + " "+ Integer.toHexString(products[3]) );
			System.out.println(products[0] + " " + products[1] + " " + products[2] + " "+ products[3] );
			result[i] = Opperations.selfXorBits(products,4);
			result[i] = Opperations.selfXorBits(products,4);
			System.out.println(Integer.toHexString(result[i]));
		}
		return result;
	} */
	
	
	static int GF_Multiply(int a , int b) {
		int product = 0;
		final int C = a;
		//System.out.println(a);
		//System.out.println(b==1);
		if(b == 1) {
			product  = a;
			
		}else if (b == 2) {
			a <<= 1;
			
			
			if((a & 0x100) != 0) {
				a^= 0x1B;
				
			}
			a&=0xFF;
			product = a;
			
			//System.out.println(product);
		}else if (b == 3) {
			
			a <<= 1;
			
			
			
			if((a & 0x100) != 0  ) {
				
				a^= 0x1B;
				
			}
			a&=0xFF;
			//System.out.println(a);
			//System.out.println(C);
			a^=C;
			
			product = a;
			
			
		}
		
		return product;
		
		
		
	}
		
	
	

	static int GFM2(int a ) {
		a <<= 1;
		if((a & 0x100) != 0  ) {
			
			a^= 0x1B;
			
		}
		a&=0xFF;
		return a;
	}
	static int Inv_GF_Multiply(int a , int b) {
		int product = 0 ;
		final int C = a;
		//System.out.println(a);
		//System.out.println(b==1);
		if(b == 9) {
			a = GFM2(a);
			a = GFM2(a);
			a = GFM2(a);
			a^=C;
			product = a;
			
			
			
		}else if (b == 11) {
			a = GFM2(a);
			a = GFM2(a);
			a^=C;
			a = GFM2(a);
			a^=C;
			product = a;
			//System.out.println(product);
		}else if (b == 13) {
			a = GFM2(a);
			a^=C;
			a = GFM2(a);
			a = GFM2(a);
			a^=C;
			product = a;
			
			
			
		}else if (b == 14) {
			a = GFM2(a);
			a^=C;
			a = GFM2(a);
			a^=C;
			a = GFM2(a);
			product = a;
			
			
			
			
		}
		
		return product;
		
		
		
	}


}
