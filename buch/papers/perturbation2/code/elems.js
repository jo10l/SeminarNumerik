

class FancyPoint extends THREE.Mesh {

    constructor(hexColor=0xff0000) {

        var r = 0.05

        var sphere_geometry = new THREE.SphereGeometry( r, 16, 16 );

        var material = new THREE.MeshLambertMaterial( {color: hexColor} );

        super( sphere_geometry, material );

    }
}

class FancyVector extends THREE.Group {

    constructor(dir, hexColor=0xff0000) {

        // normalize the direction vector (convert to vector of length 1)
        dir.normalize();

        var origin = new THREE.Vector3( 0, 0, 0 );
        var length = 1;

        var r = 0.02
        var r_head = 0.05
        var l_head = 0.2

        var cylinder_geometry = new THREE.CylinderGeometry( r, r, length-l_head, 16 );
        var cone_geometry = new THREE.ConeGeometry( r_head, l_head, 16 );

        var material = new THREE.MeshLambertMaterial( {
            color: hexColor,
            opacity: 0.5,
            transparent: true,
        } );

        var cylinder = new THREE.Mesh( cylinder_geometry, material );
        var cone = new THREE.Mesh( cone_geometry, material );

        cylinder.translateY((length-l_head)/2)
        cone.translateY(length-(l_head/2))

        super()

        this.add(cylinder)
        this.add(cone)
        var text = `${dir.x.toFixed(2)} ${dir.y.toFixed(2)} ${dir.z.toFixed(2)}`
        this.add( new Text( new THREE.Vector3(0,1,0), text))

        var matrix1 = new THREE.Matrix4().makeRotationAxis ( new THREE.Vector3(1,0,0), -Math.PI/2 )
        var matrix = new THREE.Matrix4().lookAt ( new THREE.Vector3(0,0,0), dir,  new THREE.Vector3(1,1,1))

        this.applyMatrix4( matrix1 );
        this.applyMatrix4( matrix );
    }
}

class CircleCurve extends THREE.Curve {

    getPoint( t ) {

        var tx = Math.sin( 2 * Math.PI * t) * 1;
        var ty = Math.cos( 2 * Math.PI * t) * 1;
        var tz = 0
        return new THREE.Vector3( tx, ty, tz );
    }
}

class Plane extends THREE.Group {
    constructor(dir1, dir2, hexColor) {

        // normalize the direction vector (convert to vector of length 1)
        dir1.normalize();
        dir2.normalize();

        var origin = new THREE.Vector3( 0, 0, 0 );
        var length = 1;

        var r = 0.02
        var r_head = 0.05
        var l_head = 0.2

        // var circle_geometry = new THREE.CircleGeometry( length, 96 );
        
        var path = new CircleCurve( );
        var tube_geometry = new THREE.TubeGeometry( path, 96, r_head, 16, false);
        
        var material = new THREE.MeshLambertMaterial( {
            color: hexColor,
            opacity: 0.5,
            transparent: true,
        } );

        // var circle = new THREE.Mesh( circle_geometry, material );
        var ring = new THREE.Mesh( tube_geometry, material );

        super()

        // this.add(circle)
        this.add(ring)

        var dir3 = new THREE.Vector3(0,0,0)
        dir3.crossVectors( dir1, dir2 )
        var matrix = new THREE.Matrix4().makeBasis ( dir1, dir2, dir3 )
        this.applyMatrix4( matrix );
    }
}

class Basis extends THREE.Group {

    constructor(matrix33, hexColor) {

        super();

        for (var i = 0; i < 3; i++) {
            var vec = new THREE.Vector3( matrix33[0][i], matrix33[1][i], matrix33[2][i]);
            this.add( new FancyVector( vec, hexColor) );
        }
    }

}

class EigBasis extends THREE.Group {

    constructor(e, lam, hexColor) {

        super();

        var es = []

        for (var i = 0; i < 3; i++) {
            var vec = new THREE.Vector3( e[0][i], e[1][i], e[2][i]);
            es.push(vec);
        }

        if (lam[0] == lam[1]) {
            var vec = es[2]
            this.add( new FancyVector( vec, hexColor) );
            var vec = new THREE.Vector3().copy(vec).multiplyScalar(-1)
            this.add( new FancyVector( vec, hexColor) );
            this.add( new Plane(es[0], es[1], hexColor))
        } else if (lam[1] == lam[2]) {
            var vec = es[0]
            this.add( new FancyVector( vec, hexColor) );
            var vec = new THREE.Vector3().copy(vec).multiplyScalar(-1)
            this.add( new FancyVector( vec, hexColor) );
            this.add( new Plane(es[1], es[2], hexColor))
        } else if (lam[2] == lam[0]) {
            var vec = es[1]
            this.add( new FancyVector( vec, hexColor) );
            var vec = new THREE.Vector3().copy(vec).multiplyScalar(-1)
            this.add( new FancyVector( vec, hexColor) );
            this.add( new Plane(es[2], es[0], hexColor))
        } else {
            es.forEach(function(vec) {
                this.add( new FancyVector( vec, hexColor) );
                var vec = new THREE.Vector3().copy(vec).multiplyScalar(-1)
                this.add( new FancyVector( vec, hexColor) );
            }, this);
        }

    }

}

class BasicVector extends THREE.ArrowHelper {

    constructor(dir, hexColor=0xff0000) {

        // normalize the direction vector (convert to vector of length 1)
        dir.normalize();

        var origin = new THREE.Vector3( 0, 0, 0 );
        var length = 1;

        super( dir, origin, length, hexColor );
    }
}

class CoordinateSystem extends THREE.Group{

    constructor(dir, hexColor=0xff0000) {

        var material = new THREE.LineBasicMaterial({
            color: 0x888888
        });

        var points = [];
        points.push( new THREE.Vector3( -10000, 0, 0 ) );
        points.push( new THREE.Vector3( 10000, 0, 0 ) );
        var geometry1 = new THREE.BufferGeometry().setFromPoints( points );

        points = [];
        points.push( new THREE.Vector3( 0, -10000, 0 ) );
        points.push( new THREE.Vector3( 0, 10000, 0 ) );
        var geometry2 = new THREE.BufferGeometry().setFromPoints( points );

        points = [];
        points.push( new THREE.Vector3( 0, 0, -10000 ) );
        points.push( new THREE.Vector3( 0, 0, 10000 ) );
        var geometry3 = new THREE.BufferGeometry().setFromPoints( points );

        var line1 = new THREE.Line( geometry1, material );
        var line2 = new THREE.Line( geometry2, material );
        var line3 = new THREE.Line( geometry3, material );

        super()

        this.add(line1)
        this.add(line2)
        this.add(line3)
    }
}

class Text extends THREE.Sprite {

    constructor(pos, text) {

        const canvas = document.createElement('canvas');
        canvas.style = "border : 1px"
        canvas.width = 512
        canvas.height = 512

        const ctx = canvas.getContext('2d');
        const x = 256;
        const y = 256;
        const r = 30;
        const startAngle = 0;
        const endAngle = Math.PI * 2;

        // ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
        // ctx.beginPath();
        // ctx.arc(x, y, r, startAngle, endAngle);
        // ctx.fill();

        ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
        ctx.beginPath();
        ctx.moveTo(x-r, y-r);
        ctx.lineTo(x-r, y+r);
        ctx.lineTo(x+r, y+r);
        ctx.lineTo(x+r, y-r);
        ctx.lineTo(x-r, y-r);
        ctx.fill();

        // ctx.strokeStyle = 'rgb(0, 0, 0)';
        // ctx.lineWidth = 3;
        // ctx.beginPath();
        // ctx.arc(x, y, r, startAngle, endAngle);
        // ctx.stroke();

        ctx.fillStyle = 'rgb(0, 0, 0)';
        ctx.font = '64px sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(text, x, y);

        // document.body.appendChild(canvas)

        const numberTexture = new THREE.CanvasTexture(
            canvas
        );
        
        const spriteMaterial = new THREE.SpriteMaterial({
            map: numberTexture,
            alphaTest: 0.5,
            transparent: true,
            depthTest: false,
            depthWrite: false,
            sizeAttenuation: false // true if size to be scaled with 3d perspective
        });
        
        super(spriteMaterial);
        this.position.copy(pos);
        this.scale.set(0.2, 0.2, 2);

    }
}

class Cubetransform extends THREE.Group {

    constructor(matrix33, hexColor=0x00ff00) {

        var origin = new THREE.Vector3( 0, 0, 0 );
        var length = 1;

        var r = 0.02
        var r_head = 0.05
        var l_head = 0.2

        // var geo = new THREE.BoxGeometry( 1, 1, 1 );

        // var geometry = new THREE.WireframeGeometry2( geo );
        
        // var material = new THREE.MeshLambertMaterial( {color: hexColor, transparent : true, } );

        var material = new THREE.LineBasicMaterial({
            color: hexColor,
            linewidth: 10
        });


        // var cube = new THREE.WireFrame( geometry, material );

        var points = [];
        points.push( new THREE.Vector3( 0, 0, 0 ) );
        points.push( new THREE.Vector3( 1, 0, 0 ) );
        points.push( new THREE.Vector3( 1, 1, 0 ) );
        points.push( new THREE.Vector3( 0, 1, 0 ) );
        var geometry1 = new THREE.BufferGeometry().setFromPoints( points );

        points = [];
        points.push( new THREE.Vector3( 1, 0, 0) );
        points.push( new THREE.Vector3( 1, 0, 1) );
        points.push( new THREE.Vector3( 1, 1, 1) );
        points.push( new THREE.Vector3( 1, 1, 0) );
        var geometry2 = new THREE.BufferGeometry().setFromPoints( points );

        points = [];
        points.push( new THREE.Vector3( 1, 0, 1) );
        points.push( new THREE.Vector3( 0, 0, 1) );
        points.push( new THREE.Vector3( 0, 1, 1) );
        points.push( new THREE.Vector3( 1, 1, 1) );
        var geometry3 = new THREE.BufferGeometry().setFromPoints( points );

        points = [];
        points.push( new THREE.Vector3( 0, 0, 1) );
        points.push( new THREE.Vector3( 0, 0, 0) );
        points.push( new THREE.Vector3( 0, 1, 0) );
        points.push( new THREE.Vector3( 0, 1, 1) );
        var geometry4 = new THREE.BufferGeometry().setFromPoints( points );

        var line1 = new THREE.Line( geometry1, material );
        var line2 = new THREE.Line( geometry2, material );
        var line3 = new THREE.Line( geometry3, material );
        var line4 = new THREE.Line( geometry4, material );

        super()

        this.add(line1)
        this.add(line2)
        this.add(line3)
        this.add(line4)
        // this.add(cube)

        // cylinder.translateY((length-l_head)/2)

        var matrix0 = new THREE.Matrix4().makeTranslation ( -0.5, -0.5, -0.5)

        // var matrix = new THREE.Matrix4().set(
        //     matrix33[0][0],
        //     matrix33[1][0],
        //     matrix33[2][0],
        //     0,
        //     matrix33[0][1],
        //     matrix33[1][1],
        //     matrix33[2][1],
        //     0,
        //     matrix33[0][2],
        //     matrix33[1][2],
        //     matrix33[2][2],
        //     0,
        //     0,0,0,1
        // )

        this.matrixAutoUpdate = false;

        var matrix = new THREE.Matrix4().set(
            matrix33[0][0],
            matrix33[0][1],
            matrix33[0][2],
            0,
            matrix33[1][0],
            matrix33[1][1],
            matrix33[1][2],
            0,
            matrix33[2][0],
            matrix33[2][1],
            matrix33[2][2],
            0,
            0,0,0,1
        )

        // matrix.multiply(matrix0)

        // this.applyMatrix4( matrix0 );
        this.applyMatrix4( matrix );

        console.log(matrix33)
        console.log(matrix)
    }
}
