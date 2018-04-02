import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.URL;
import java.nio.file.Path;
import java.util.List;
import java.io.File;
import java.util.ArrayList;
import java.io.BufferedReader;


class Unpacking{
    public static void main(String[] args) throws Exception {
        // File csv = new File("1.csv");
        // Scanner scanner = new Scanner(csv);
        // String splitBy = ",";
        // ArrayList<String> list = new ArrayList<String>();
        // while(scanner.hasNextLine()){
        //     String[] line = list.split(splitBy);
        //     System.out.println(line);
        // }
        String csv = "1.csv";
        BufferedReader br = null;
        String line = "";
        String splitBy = ",";

        try{
            br = new BufferedReader(new FileReader(csv));
            while((line = br.readLine())!=null){
                String[] lineArr = line.split(splitBy);
                for(String s : lineArr){
                    System.out.println(s);
                }
                
            }
        }
        catch(Exception e){
            System.out.println(e);
        }

    }
}
