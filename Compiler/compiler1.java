import java.lang.*;
import java.util.*;
import java.io.*;

class compiler1{


public static void main(String[] args)
{
try
	{
	ArrayList<String> tokens = new ArrayList<String>();
	BufferedReader br = new BufferedReader(new FileReader("/home/varad/Desktop/Btech/Compiler/Input.txt"));
	String line = null;

	while((line=br.readLine())!=null)
		{
		line = line.trim().replaceAll(";$","");
		Collections.addAll(tokens,line.split(",|\\(|\\)|\\ "));
		}
	System.out.println(tokens);
	}
catch(Exception e)
	{
	System.out.println(e);
	}
}
		}
