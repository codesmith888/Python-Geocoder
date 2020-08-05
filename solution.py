import geocoder


destinations = {
  "Space Needle",
  "Crater Lake",
  "Golden Gate Bridge",
  "Yosemite National Park",
  "Las Vegas, Nevada",
  "Grand Canyon National Park",
  "Aspen, Colorado",
  "Mount Rushmore",
  "Yellowstone National Park",
  "Sandpoint, Idaho",
  "Banff National Park",
  "Capilano Suspension Bridge"
}

for location in destinations:
  g = geocoder.arcgis(f'{location}')
  print(f'{location}' " is located at " f'{(g.latlng)}')
