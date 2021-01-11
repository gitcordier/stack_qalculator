/* 
  pn/stack/<stack_id>  GET: Compute
 */

/* stack, operator: */
let stack_id_compute = document.getElementById("stack_id_compute").value;
let op               = document.getElementById("op").value;

/*fetch API: */
document.getElementById("button_compute").addEventListener("click", async _=> {
  event.preventDefault();
  await fetch("http://localhost:5000/rpn/stack/"+stack_id_compute+"?op="+op ,{
    method: 'GET', 
    headers: {
      'Content-Type': 'application/json'
    },
  }).then(response => {
    if (response.ok) { console.log("OK"); return response.json();}
    else {
      console.log("Something went wrong.");
    }
});
})

/* 
   rpn/stack/<stack_id>: UPDATE. Empty/reset stack.
 */
let stack_id_empty = document.getElementById("stack_id_empty").value;

/*fetch API: */
document.getElementById("button_empty_stack").addEventListener("click", async _ => {
  event.preventDefault();

  await fetch("http://localhost:5000/rpn/stack/" + stack_id_empty, {
    method: 'PUT', 
    headers: {
      'Content-Type': 'application/json'
    },
  }).then(response => {
    if (response.ok) { console.log("OK"); return response.json();}
    else {
      console.log("Something went wrong.");
    }
});
})