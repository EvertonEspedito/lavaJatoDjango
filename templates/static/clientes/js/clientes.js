function add_carro(){

    container = document.getElementById("form-carro");

    const html = `
        <br>
        <div class="row">
            <div class="col-md">
                <input type="text" placeholder="Carro" class="form-control" name="carro">
            </div>
            <div class="col-md">
                <input type="text" placeholder="Placa" class="form-control" name="placa">
            </div>
        </div>
    `;

    container.innerHTML += html


}