const { collector } = require("./build");
const { join } = require("path");
const fs = require('fs');
(async () => {
 const EMULATE_DEVICE = "";
          // Save the results to a folder
        let OUT_DIR = true;
        const URL = process.argv[2];
        var log = process.argv[3];
        const hashes = process.argv[4];
        console.log(hashes)
        var url_list = URL.split(",");
        var url_hash_list = hashes.split(",");
        var today = new Date();
        var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
        var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
        var dateTime = date+' '+time;
        log = log + dateTime  + " Decoding of encoded URL started \n";
        console.log(log);
        for(let i =0;i<url_list.length;i++)
        {
     date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
        time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
        dateTime = date+ " " +time;
        var url_base64 = url_list[i];
        var buff = Buffer.from(url_base64, 'base64');
        var url = buff.toString('utf-8');
        date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
        time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
        dateTime = date+ " " +time;
        log = log + dateTime + " " + url_base64 + " decoded to " + url + "\n";
        console.log(dateTime + " " + url_base64 + " decoded to " + url + "\n")
        var defaultConfig = {
        inUrl: url, //remove https
        numPages: 0,
        headless: true,
        emulateDevice: EMULATE_DEVICE,
        };
        fs.writeFileSync('logfile.txt',log);
        var destination_folder ="output_directory/"+ url_hash_list[i]
	var result = await collector(
        OUT_DIR
        ? { ...defaultConfig, ...{ outDir: join(__dirname, destination_folder) } }
         : defaultConfig);
                  if (OUT_DIR) {
                              console.log( `For captured data please look in ${{join(__dirname, destination_folder)}`);
                            }
        }
})();
