#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# system utilities methods
# IMIO <support@imio.be>
#

import os
import sys


def verbose(msg):
    print '>> %s' % msg


def error(msg):
    print >> sys.stderr, '!! %s' % msg


def trace(TRACE, msg):
    if not TRACE:
        return
    print "TRACE:'%s'" % msg

#------------------------------------------------------------------------------


def write_to(outfiles, key, line):
    """
        Open output file and write line (adding line feed)
        outfiles param: dic containing this struct {'key': {'file': 'filepath', 'header': 'First line'}}
    """
    if not 'fh' in outfiles[key]:
        filename = outfiles[key]['file']
        try:
            outfiles[key]['fh'] = open(filename, 'w')
            if 'header' in outfiles[key] and outfiles[key]['header']:
                outfiles[key]['fh'].write("%s\n" % outfiles[key]['header'])
        except IOError, m:
            error("Cannot create '%s' file: %s" % (filename, m))
            return
    outfiles[key]['fh'].write("%s\n" % line)

#------------------------------------------------------------------------------


def close_outfiles(outfiles):
    """ Close the outfiles """
    for key in outfiles.keys():
        if 'fh' in outfiles[key]:
            outfiles[key]['fh'].close()
#            verbose("Output file '%s' generated" % outfiles[key]['file'])

#------------------------------------------------------------------------------


def read_file(filename, strip_chars='', skip_empty=False):
    """ read a file and return lines """
    try:
        thefile = open(filename, 'r')
    except IOError:
        error("! Cannot open %s file" % filename)
        return
    lines = []
    for line in thefile.readlines():
        line = line.strip('\n')
        if strip_chars:
            line = line.strip(strip_chars)
        if skip_empty and not line:
            continue
        lines.append(line)
    thefile.close()
    return lines

#------------------------------------------------------------------------------


def read_dir(dirpath, with_path=False, only_folders=False):
    """ Read the dir and return files """
    files = []
    for filename in os.listdir(dirpath):
        if only_folders and not os.path.isdir(os.path.join(dirpath, filename)):
            continue
        if with_path:
            files.append(os.path.join(dirpath, filename))
        else:
            files.append(filename)
    return files

#------------------------------------------------------------------------------


def read_dir_filter(dirpath, with_path=False, extensions=[], only_folders=False):
    """ Read the dir and return some files """
    files = []
    for filename in read_dir(dirpath, with_path=with_path, only_folders=only_folders):
        basename, ext = os.path.splitext(filename)
        if ext and ext.startswith('.'):
            ext = ext[1:]
        if extensions and ext not in extensions:
            continue
        files.append(filename)
    return files

#------------------------------------------------------------------------------


def read_dir_extensions(dirpath):
    """ Read the dir and return extensions """
    extensions = []
    for filename in read_dir(dirpath):
        basename, ext = os.path.splitext(filename)
        if ext and ext.startswith('.'):
            ext = ext[1:]
        if ext not in extensions:
            extensions.append(ext)
    extensions.sort()
    return extensions

#------------------------------------------------------------------------------


def runCommand(cmd):
    """ run an os command and get back the stdout and stderr outputs """
    os.system(cmd + ' >_cmd_pv.out 2>_cmd_pv.err')
    stdout = stderr = []
    try:
        if os.path.exists('_cmd_pv.out'):
            ofile = open('_cmd_pv.out', 'r')
            stdout = ofile.readlines()
            ofile.close()
            os.remove('_cmd_pv.out')
        else:
            error("File %s does not exist" % '_cmd_pv.out')
    except IOError:
        error("Cannot open %s file" % '_cmd_pv.out')
    try:
        if os.path.exists('_cmd_pv.err'):
            ifile = open('_cmd_pv.err', 'r')
            stderr = ifile.readlines()
            ifile.close()
            os.remove('_cmd_pv.err')
        else:
            error("File %s does not exist" % '_cmd_pv.err')
    except IOError:
        error("Cannot open %s file" % '_cmd_pv.err')
    return(stdout, stderr)

#------------------------------------------------------------------------------


def load_dic(infile, dic):
    """
        load a dictionary from a file
    """
    if os.path.exists(infile):
        ofile = open(infile, 'r')
        dic.update(eval(ofile.read()))
        ofile.close()

#------------------------------------------------------------------------------


def dump_dic(outfile, dic):
    """
        dump a dictionary to a file
    """
    ofile = open(outfile, 'w')
    ofile.write(str(dic))
    ofile.close()

#------------------------------------------------------------------------------


def human_size(nb):
    sizeletter = {1: 'k', 2: 'M', 3: 'G', 4: 'T'}
    for x in range(1, 4):
        quot = nb // 1024 ** x
        if quot < 1024:
            break
    return "%.1f%s" % (float(nb) / 1024 ** x, sizeletter[x])

#------------------------------------------------------------------------------


def disk_size(path, pretty=True):
    """
        return disk size of path content
    """
    cmd = "du -s"
    if pretty:
        cmd += 'h'
    (cmd_out, cmd_err) = runCommand("%s %s" % (cmd, path))
    for line in cmd_out:
        (size, path) = line.strip().split()
        return size
    return 0
