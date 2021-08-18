const { join } = require("path");

(async () => {
  const EMULATE_DEVICE = "";

  // Save the results to a folder
  let OUT_DIR = true;

  // The URL to test
  const URL = process.argv[2];
  console.log(process.argv[2]);
  var url_list = URL.split(",");
  //const url1 = string[0];
  //const url2 = string[1];

  for(let i =0;i<url_list.length;i++)
{
    var url_base64 = url_list[i];
    var buff = Buffer.from(url_base64, 'base64');
    var url = buff.toString('ascii');
    var defaultConfig = {
    inUrl: `http://${url}`,
    numPages: 0,
    headless: true,
    emulateDevice: EMULATE_DEVICE,
  };
    var destination_dict = url_list[i]
        var result = await collector(
    OUT_DIR
      ? { ...defaultConfig, ...{ outDir: join(__dirname, destination_dict) } }
      : defaultConfig
  );
  if (OUT_DIR) {
    console.log(
      `For captured data please look in ${join(__dirname, destination_dict)}`
    );
  }
}
})();