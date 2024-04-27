import { Feature, Map, View } from "ol";
import TileLayer from "ol/layer/Tile";
import { fromLonLat } from "ol/proj";
import OSM from "ol/source/OSM";
import { Circle, Point } from "ol/geom";
import { Style, Stroke, Fill } from "ol/style";
import "./style.css";
import { Vector } from "ol/source";
import CircleStyle from "ol/style/Circle";
import VectorSource from "ol/source/Vector";
import VectorLayer from "ol/layer/Vector";

let features = [];

let posArr = [
  {
    lon: 76.286352,
    lat: 10.362204,
  },
  {
    lon: 76.287409,
    lat: 10.362177,
  },
  {
    lon: 76.287751,
    lat: 10.361483,
  },
  {
    lon: 76.287588,
    lat: 10.36074,
  },
  {
    lon: 76.288142,
    lat: 10.360047,
  },
  {
    lon: 76.290279,
    lat: 10.35936,
  },
];

posArr.map((pos) => {
  features.push(
    new Feature({
      geometry: new Point(fromLonLat([pos.lon, pos.lat])),
    })
  );
});
const vectorSource = new VectorSource({
  features,
});
const vectorLayer = new VectorLayer({
  source: vectorSource,
  style: new Style({
    image: new CircleStyle({
      radius: 7,
      fill: new Fill({ color: "red" }),
    }),
  }),
});

const map = new Map({
  layers: [
    new TileLayer({
      source: new OSM(),
    }),
    vectorLayer,
  ],
  target: "map", // assuming there's an element with id "map" in your HTML
  view: new View({
    center: fromLonLat([76.285927, 10.360338]),
    zoom: 17,
  }),
});
