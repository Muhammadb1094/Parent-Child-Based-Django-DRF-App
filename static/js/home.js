$(function(){
    var base_url = document.getElementById("base_url").value;

    fetch( base_url + '/api/topics')
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        console.log(data);

        let list = document.getElementById("myList");

        if (data.length ==0){

            let li = document.createElement("li");
            li.innerText = "Nothing Added Yet!";

            list.appendChild(li);
        }
         function def(json){
                  json.forEach((item)=>{

                      let li = document.createElement("li");
                      li.innerText = item["title"] ;

                      let a = document.createElement("a");
                      a.value = "ADD CHILD";


                      list.appendChild(li);
                      list.append(a);

                  if(item["childs"].length != 0){

                       return def(item["childs"])
                  }
                  else
                  {

                    return false;
                  }

                });
         }
         def(data);

      });

});