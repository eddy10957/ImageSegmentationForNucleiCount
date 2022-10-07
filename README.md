# Image Segmentation For Nuclei Count
Progetto per l'esame di Sistemi Multimediali.

Nel seguente elaborato, verrà analizzato un sistema per la conta delle cellule presenti in un'immagine di un campione prodotta da un microscopio confocale. Il processo della conta delle cellule è alla base di numerosi esperimenti in ambito biologico o medico, le immagini analizzate sono state prese da campioni di cellule neuronali.

## Gallery:

<table>
  <tr>
     <td>Opening</td>
     <td>Dilation</td>
     <td>Erosion</td>
  </tr>
  <tr>
    <td><img  width="300" height="300" src="assets/dapi/risultati/16_apertura.png"></td>
    <td><img  width="300" height="300" src="assets/dapi/risultati/16_surebg.png"></td>
    <td><img  width="300" height="300" src="assets/dapi/risultati/16_surefg_thresh.png"></td>
  </tr>
  <tr>
    <td>Unknow Regions</td>
     <td>Watershed</td>
     <td>Final Result</td>
  </tr>
  <tr>
    <td><img  width="300" height="300" src="assets/dapi/risultati/16_unknown.png"></td>
    <td><img  width="300" height="300" src="assets/dapi/risultati/16_watershed.png"></td>
    <td><img  width="300" height="300" src="assets/dapi/risultati/16.png"></td>
  </tr>
 </table>

