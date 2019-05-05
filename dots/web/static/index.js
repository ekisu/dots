var vm = new Vue({
    el: '#main',
    data: {
        output: "",

        image_file: null,
        threshold_function: "",
        output_function: "",
        invert: false,
        resize_factor: 1
    },
    methods: {
        submit: async function(e) {
            e.preventDefault();

            let formData = new FormData();

            formData.append("image", this.image_file);
            formData.append("threshold_function", this.threshold_function);
            formData.append("output_function", this.output_function);
            formData.append("resize_factor", this.resize_factor);
            formData.append("invert", this.invert);

            let response = await fetch("/convert", {
                method: "POST",
                headers: {
                    "Accept": "application/json"
                },
                body: formData
            });

            if (response.status != 200) {
                alert("Error while converting");
                return;
            }

            let json = await response.json();
            this.output = json.output.join("\n");
        },
        handleFile: function(e) {
            if (e.target.files.length > 0)
                this.image_file = e.target.files[0];
            else
                this.image_file = null;
        }
    },
    computed: {
        canSubmit: function() {
            return this.image_file !== null
                && this.threshold_function != ""
                && this.output_function != "";
        }
    },
    delimiters: ['[[', ']]']
})