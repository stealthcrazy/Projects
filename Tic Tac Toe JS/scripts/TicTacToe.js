
let boxes = document.querySelectorAll('.square');
let resetBtn = document.getElementById('reset');
console.log(boxes)

let turn = 0;


function Check(boxes,turn,){
    let counter = 0;
    let row = [];
    let winCon = false;
    
    let player = 'O';
    if(turn%2 == 0){
        player = 'X';
    }else{
        player = 'O';
    };
    let winStatement = `Player ${player} Wins!  `
    for(let i = 0; i<9;i++){
        
        row.push(boxes[i].innerHTML);

    };
    let rows = [[row[0],row[1],row[2]],
                [row[3],row[4],row[5]],
                [row[6],row[7],row[8]]
                ];
   
        
    for(let j = 0;j<3;j++){
        
        if (rows[j][0] === 'O' && rows[j][1] === 'O' && rows[j][2] === 'O' ){
            
            document.getElementById('result').innerHTML = winStatement;
            winCon = true;
        } if (rows[j][0] === 'X' && rows[j][1] === 'X' && rows[j][2] === 'X' ){
            
            document.getElementById('result').innerHTML = winStatement;
            winCon = true;
        }if (rows[0][j] === 'O' && rows[1][j] === 'O' && rows[2][j] === 'O' ){
            
            document.getElementById('result').innerHTML = winStatement;
            winCon = true;
        } if (rows[0][j] === 'X' && rows[1][j] === 'X' && rows[2][j] === 'X' ){
            
            document.getElementById('result').innerHTML = winStatement;
            winCon = true;
        };
    };
    if (rows[0][0] === 'X' && rows[1][1] === 'X' && rows[2][2] === 'X' ){
            
        document.getElementById('result').innerHTML = winStatement;
        winCon = true;
    }if (rows[0][0] === 'O' && rows[1][1] === 'O' && rows[2][2] === 'O' ){
            
        document.getElementById('result').innerHTML = winStatement;
        winCon = true;
    }if (rows[0][2] === 'X' && rows[1][1] === 'X' && rows[2][0] === 'X' ){
            
        document.getElementById('result').innerHTML = winStatement;
        winCon = true;
    }if (rows[0][2] === 'O' && rows[1][1] === 'O' && rows[2][0] === 'O' ){
            
        document.getElementById('result').innerHTML = winStatement;
        winCon = true;
    };
    
    console.log(rows)
    return winCon;
}
let won = false
boxes.forEach(function (element, i) {
    element.addEventListener('click',function(){
        
        console.log(`${i+1} clicked`)
        if (won === false){
            if(element.innerHTML === ''){
                if (turn%2 === 0){
                    element.innerHTML = 'O';
                }else{
                    element.innerHTML = 'X';
                };
            };
            turn+=1
        }
        
        won = Check(boxes,turn);
        resetBtn.addEventListener('click',function(){
            boxes.forEach(function(ChildE){
                ChildE.innerHTML = '';
                document.getElementById('result').innerHTML = '';
                won =false;
            });
        })
        
        
        
    })
});

