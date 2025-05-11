function add_carro(){

    container = document.getElementById("form-carro");

    const html = `
        <br>
        <div class="row">
            <div class="col-md">
                <input type="text" placeholder="Carro/Moto" class="form-control" name="tipo">
            </div>
            <div class="col-md">
                <input type="text" placeholder="Modelo" class="form-control" name="modelo">
            </div>
            <div class="col-md">
                <input type="text" placeholder="Placa" class="form-control" name="placa">
            </div>
            <div class="col-md">
                <input type="number" placeholder="Ano" class="form-control" name="ano">
            </div>
        </div>
    `;

    container.innerHTML += html


}