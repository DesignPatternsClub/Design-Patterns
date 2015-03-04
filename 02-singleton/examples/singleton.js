var mySingleton = (function () {
    var instance;

    function init() {
        var privateVariable = "I’m private";
        var id = Math.floor(Math.random() * 10000);

        function privateMethod() {}

        return {
            publicProperty: "I am public",
            publicMethod: function () {},
            publicId: function () {
                return id;
            }
        };
    };

    return {
        getInstance: function () {
            if (!instance) {
                instance = init();
            }

            return instance;
        }
    };
})();

console.log(mySingleton);
console.log(mySingleton.getInstance());
console.log(mySingleton.getInstance().publicId());
console.log(mySingleton.getInstance().publicId());
