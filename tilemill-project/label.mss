#routes2::text { [zoom >= 14] { [count >= 10] {
  text-name: [route_short_name];
  //text-name: [count];
  text-face-name: @futura_med;
  text-placement: line;
  text-halo-radius: 2;
  
  [agency_id = 'GMS'], [agency_id = 'RMS'], [agency_id = 'SWI'] {
  	text-fill: red;
  }
  [agency_id = 'CAL'], [agency_id = 'FPR'], [agency_id = 'GMN'] {
  	text-fill: blue;
  }
  [agency_id = 'NOR'], [agency_id = 'MTL'] {
  	text-fill: green;
  }    
} } }