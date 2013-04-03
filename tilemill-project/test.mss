@futura_med: "Futura Medium","Function Pro Medium","Ubuntu Regular","Trebuchet MS Regular","DejaVu Sans Book";
@futura_italic: "Futura Medium Italic","Function Pro Medium Italic","Ubuntu Italic","Trebuchet MS Italic","DejaVu Sans Oblique";
@futura_bold: "Futura Bold","Function Pro Bold","Ubuntu Bold","Trebuchet MS Bold","DejaVu Sans Bold";

/*
#routes {
  line-color: black;
  //text-name: [service];
  //text-face-name: @futura_med;
  [operator = 'Stagecoach Manchester bus'], [operator = 'Stagecoach Wigan bus'], [operator = 'Stagecoach In Lancashire bus'] {
  	line-color: red;
  }
  [operator = 'First bus'], [operator = 'First Yorkshire West bus'] {
  	line-color: blue;
  }
  [operator = 'Arriva North West bus'] {
  	line-color: green;  
  }
  [operator = 'Metrolink tram'] {
  	line-color: yellow;
  }
}
*/

#routes2 {
  line-color: black;
  
  [agency_id = 'GMS'], [agency_id = 'RMS'], [agency_id = 'SWI'] {
  	line-color: red;
  }
  [agency_id = 'CAL'], [agency_id = 'FPR'], [agency_id = 'GMN'] {
  	line-color: blue;
  }
  [agency_id = 'NOR'], [agency_id = 'MTL'] {
  	line-color: green;
  }
  
  [count>=0] { line-width: 0 }
  [count>=10] { line-width: 1 }
  [count>=500] { line-width: 2 }
  [count>=1000] { line-width: 3 }
  [count>=2000] { line-width: 4 }
  [count>=4000] { line-width: 5 }
  [offset=0] { line-offset: 0 }
  [offset>0] { line-offset: 1 }
  [offset>1] { line-offset: 2 }
  [offset>2] { line-offset: 3 }
  [offset>3] { line-offset: 4 }
  [offset>4] { line-offset: 5 }
  [offset>5] { line-offset: 6 }
  [offset>6] { line-offset: 7 }
  [offset>7] { line-offset: 8 }
  [offset>8] { line-offset: 9 }
  [offset>9] { line-offset: 10 }
  
  [zoom >=15] {
  [count>=0] { line-width: 0 }
  [count>=10] { line-width: 1 }
  [count>=250] { line-width: 2 }
  [count>=500] { line-width: 4 }
  [count>=1000] { line-width: 6 }
  [count>=2000] { line-width: 8 }
  [count>=4000] { line-width: 10 }
  [offset=0] { line-offset: 0 }
  [offset>0] { line-offset: 1 }
  [offset>0.5] { line-offset: 2 }
  [offset>1] { line-offset: 4 }
  [offset>2] { line-offset: 6 }
  [offset>3] { line-offset: 8 }
  [offset>4] { line-offset: 10 }
  [offset>5] { line-offset: 12 }
  [offset>6] { line-offset: 14 }
  [offset>7] { line-offset: 16 }
  [offset>8] { line-offset: 18 }
  [offset>9] { line-offset: 20 } 
  }

}
