var scene = new THREE.Scene();
// var camera = new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight);
zoom = 300
var camera = new THREE.OrthographicCamera( -window.innerWidth/zoom, window.innerWidth/zoom, window.innerHeight/zoom, -window.innerHeight/zoom, -10, 100 );
// camera.position.z = 5;

camera.position.set( 2, 2, 2 );
camera.lookAt( 0, 0, 0 );
camera.up.set( 0, 0, 1 );

var renderer = new THREE.WebGLRenderer({antialias: true});
renderer.setSize(window.innerWidth,window.innerHeight);
renderer.setClearColor (0x000000, 1);
renderer.setClearColor (0xffffff, 1);

document.body.append(renderer.domElement);

// var geometry = new THREE.BoxGeometry(1,1,1);
// // var material = new THREE.MeshBasicMaterial({color: 0xff0000});
// var material = new THREE.MeshLambertMaterial();
// material.color.setHSL(0, 1, .9);  // red
// material.flatShading = true;
// var cube = new THREE.Mesh(geometry,material);
// scene.add(cube);

// cube.position.z = 0;
// cube.rotation.x = 10;
// cube.rotation.y = 5;

var spotLight = new THREE.SpotLight(0x999999);
spotLight.position.set(-0, 30, 60);
spotLight.castShadow = true;
spotLight.intensity = 1;
scene.add(spotLight);

var light = new THREE.AmbientLight( 0x777777 ); // soft white light
scene.add( light );


var x = new THREE.Vector3( 1, 0, 0 );
var y = new THREE.Vector3( 0, 1, 0 );
var z = new THREE.Vector3( 0, 0, 1 );

var xx = new THREE.Vector3( 1.5, 0, 0 );
var yy = new THREE.Vector3( 0, 1.5, 0 );
var zz = new THREE.Vector3( 0, 0, 1.5 );


// scene.add( new BasicVector(x, 0xff0000) );
// scene.add( new BasicVector(y, 0x00ff00) );
// scene.add( new BasicVector(z, 0x0000ff) );

// scene.add( new FancyVector( x, 0xff0000)) ; 
// scene.add( new FancyVector( y, 0x00ff00));
// scene.add( new FancyVector( z, 0x0000ff));
// scene.add( new FancyPoint(scene, 0xffffff));

json.elems.forEach( function(elem){

	if (elem.type == "basis") {
		var hexColor = parseInt(elem.color.replace(/^#/, ''), 16)
		scene.add( new Basis( elem.data, hexColor) )
	} else if (elem.type == "eigbasis") {
		var hexColor = parseInt(elem.color.replace(/^#/, ''), 16)
		scene.add( new EigBasis( elem.e, elem.lam, hexColor) )
	} else if (elem.type == "transform") {
		var hexColor = parseInt(elem.color.replace(/^#/, ''), 16)
		scene.add( new Cubetransform( elem.data, hexColor) )
	}
})

scene.add (new Text(xx, "x"))
scene.add (new Text(yy, "y"))
scene.add (new Text(zz, "z"))

// scene.add (new Plane(z, x))



// scene.add( new CoordinateSystem())


renderer.render(scene,camera);

var controls = new THREE.OrbitControls( camera, renderer.domElement );

function animate() {

	requestAnimationFrame( animate );

	// required if controls.enableDamping or controls.autoRotate are set to true
	controls.update();

	renderer.render( scene, camera );

}

animate()